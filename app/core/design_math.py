import math
import re
from collections import Counter


EPSILON = 1e-9
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
WORD_RE = re.compile(r"[a-z0-9]+(?:[-_][a-z0-9]+)*", re.IGNORECASE)


class TextVectorizer:
    """Small dependency-free vectorizer for mixed Chinese and Latin design briefs."""

    def __init__(self, ngram_range=(1, 3)):
        self.ngram_range = ngram_range

    def tokens(self, text):
        text = str(text or "").lower()
        features = Counter()

        for word in WORD_RE.findall(text):
            features[word] += 1.0
            for part in re.split(r"[-_]", word):
                if len(part) > 1:
                    features[part] += 0.5

        chars = CJK_RE.findall(text)
        for char in chars:
            features[char] += 0.2

        joined = "".join(chars)
        start, end = self.ngram_range
        for n in range(max(2, start), max(2, end) + 1):
            if len(joined) >= n:
                for index in range(len(joined) - n + 1):
                    features[joined[index:index + n]] += 1.0

        return features


def cosine(left, right):
    if not left or not right:
        return 0.0
    dot = sum(left[key] * right.get(key, 0.0) for key in left)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    return dot / (left_norm * right_norm + EPSILON)


def jaccard(left, right):
    left_keys = set(left)
    right_keys = set(right)
    if not left_keys or not right_keys:
        return 0.0
    return len(left_keys & right_keys) / (len(left_keys | right_keys) + EPSILON)


def sigmoid(value):
    if value >= 0:
        exp_value = math.exp(-value)
        return 1 / (1 + exp_value)
    exp_value = math.exp(value)
    return exp_value / (1 + exp_value)


def weighted_sum(metrics, weights):
    total_weight = sum(abs(value) for value in weights.values()) + EPSILON
    return sum(float(metrics.get(key, 0.0)) * weight for key, weight in weights.items()) / total_weight


class ScoreNormalizer:
    @staticmethod
    def minmax(scores):
        values = list(scores)
        if not values:
            return []
        low = min(values)
        high = max(values)
        if abs(high - low) < EPSILON:
            return [1.0 for _ in values]
        return [(value - low) / (high - low) for value in values]

    @staticmethod
    def softmax(scores, temperature=1.0):
        values = list(scores)
        if not values:
            return []
        temperature = max(float(temperature), EPSILON)
        high = max(values)
        exps = [math.exp((value - high) / temperature) for value in values]
        total = sum(exps) + EPSILON
        return [value / total for value in exps]

    @staticmethod
    def entropy(probabilities):
        probs = [value for value in probabilities if value > EPSILON]
        if len(probs) <= 1:
            return 0.0
        raw = -sum(value * math.log(value) for value in probs)
        return raw / math.log(len(probs))

    @staticmethod
    def confidence(best_probability, second_probability, entropy):
        margin = max(0.0, best_probability - second_probability)
        certainty = 1.0 - min(1.0, entropy)
        return min(0.99, max(0.5, 0.5 + 0.34 * margin + 0.16 * certainty))


def pareto_front(items, objective_keys):
    front = []
    for index, item in enumerate(items):
        dominated = False
        for other_index, other in enumerate(items):
            if other_index == index:
                continue
            at_least = all(_objective(other, key) >= _objective(item, key) - EPSILON for key in objective_keys)
            strictly = any(_objective(other, key) > _objective(item, key) + EPSILON for key in objective_keys)
            if at_least and strictly:
                dominated = True
                break
        if not dominated:
            front.append(index)
    return front


def topsis_rank(items, objective_weights):
    if not items:
        return []
    keys = list(objective_weights)
    columns = {}
    for key in keys:
        values = [_objective(item, key) for item in items]
        norm = math.sqrt(sum(value * value for value in values)) + EPSILON
        columns[key] = [value / norm for value in values]

    ideal = {key: max(columns[key]) for key in keys}
    anti = {key: min(columns[key]) for key in keys}
    ranked = []
    for index, item in enumerate(items):
        distance_to_ideal = 0.0
        distance_to_anti = 0.0
        for key in keys:
            weight = objective_weights[key]
            value = columns[key][index]
            distance_to_ideal += weight * (value - ideal[key]) ** 2
            distance_to_anti += weight * (value - anti[key]) ** 2
        distance_to_ideal = math.sqrt(distance_to_ideal)
        distance_to_anti = math.sqrt(distance_to_anti)
        closeness = distance_to_anti / (distance_to_ideal + distance_to_anti + EPSILON)
        ranked.append((index, closeness))
    return ranked


class MultiObjectiveRanker:
    def rank(self, items, objective_weights):
        if not items:
            return []
        objective_keys = list(objective_weights)
        normalized_by_key = {}
        for key in objective_keys:
            normalized_by_key[key] = ScoreNormalizer.minmax([_objective(item, key) for item in items])

        topsis_scores = dict(topsis_rank(items, objective_weights))
        front = set(pareto_front(items, objective_keys))
        ranked_items = []
        for index, item in enumerate(items):
            normalized = {key: normalized_by_key[key][index] for key in objective_keys}
            utility = weighted_sum(normalized, objective_weights)
            final_score = (0.55 * utility) + (0.40 * topsis_scores.get(index, 0.0)) + (0.05 if index in front else 0.0)
            clone = dict(item)
            clone["metrics"] = dict(item.get("metrics", {}))
            clone["normalized_metrics"] = {key: round(value, 4) for key, value in normalized.items()}
            clone["utility_score"] = round(utility, 4)
            clone["topsis_score"] = round(topsis_scores.get(index, 0.0), 4)
            clone["pareto_front"] = index in front
            clone["final_score"] = round(final_score, 4)
            ranked_items.append(clone)

        ranked_items.sort(key=lambda item: item["final_score"], reverse=True)
        for rank, item in enumerate(ranked_items, start=1):
            item["rank"] = rank
        return ranked_items


class ConstraintPenaltyModel:
    RISK_WEIGHTS = {
        "identity_drift": 0.95,
        "cad_topology_drift": 0.95,
        "text_error_or_mojibake": 0.85,
        "fragmented_visual": 0.75,
        "source_geometry_drift": 0.9,
        "generic_symbol_stack": 0.65,
    }

    MITIGATION_WEIGHTS = {
        "identity_lock": 0.65,
        "face_identity": 0.25,
        "body_anatomy": 0.2,
        "source_geometry_lock": 0.65,
        "wall_topology": 0.25,
        "door_window_openings": 0.25,
        "text_accuracy_lock": 0.55,
        "exact text policy": 0.25,
        "one dominant visual anchor": 0.25,
        "controlled density": 0.2,
    }

    def penalty_vector(self, intent, constraints):
        risks = set(intent.risks)
        hard = set(constraints.get("hard_constraints", ()))
        soft = set(constraints.get("soft_goals", ()))
        controls = set(constraints.get("risk_controls", ()))
        mitigations = hard | soft | controls

        risk_load = sum(self.RISK_WEIGHTS.get(risk, 0.45) for risk in risks)
        mitigation_strength = sum(self.MITIGATION_WEIGHTS.get(item, 0.08) for item in mitigations)
        domain_complexity = 0.15 * max(0, len(intent.domains) - 1)
        context_complexity = 0.1 * max(0, len(intent.project_contexts) - 1)
        generic_penalty = 0.25 if intent.domains and intent.domains[0] == "general-design" else 0.0
        residual = max(0.0, risk_load + domain_complexity + context_complexity + generic_penalty - mitigation_strength)
        residual = min(1.0, residual / 2.25)
        hard_load = min(1.0, len(hard) / 12)
        specificity = min(1.0, (len(hard) + len(soft) + len(controls)) / 18)
        return {
            "risk_load": round(risk_load, 4),
            "mitigation_strength": round(mitigation_strength, 4),
            "domain_complexity": round(domain_complexity, 4),
            "context_complexity": round(context_complexity, 4),
            "generic_penalty": round(generic_penalty, 4),
            "hard_constraint_load": round(hard_load, 4),
            "specificity_score": round(specificity, 4),
            "residual_risk": round(residual, 4),
            "constraint_satisfaction": round(1.0 - residual, 4),
        }


def _objective(item, key):
    if key in item:
        return float(item.get(key, 0.0))
    return float(item.get("metrics", {}).get(key, 0.0))
