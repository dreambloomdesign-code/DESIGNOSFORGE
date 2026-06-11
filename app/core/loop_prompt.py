from dataclasses import asdict, dataclass


LOOP_PROMPT_PACK_VERSION = "2.0.0-loop.1"


@dataclass(frozen=True)
class LoopProfile:
    loop_type: str
    title: str
    purpose: str
    triggers: tuple[str, ...]
    state_schema: tuple[str, ...]
    critique_axes: tuple[str, ...]
    revision_axes: tuple[str, ...]
    stop_conditions: tuple[str, ...]
    next_prompt_template: str
    negative_controls: tuple[str, ...]


@dataclass(frozen=True)
class LoopDetection:
    active: bool
    loop_type: str
    confidence: float
    trigger_hits: tuple[str, ...]
    score_table: dict

    def to_dict(self):
        return asdict(self)


LOOP_PROFILES = {
    "self_refine_loop": LoopProfile(
        loop_type="self_refine_loop",
        title="Self-refine prompt iteration",
        purpose="Draft, critique, revise, and rescore a prompt while keeping the original brief stable.",
        triggers=("loop", "循环", "闭环", "迭代", "反复", "多轮", "自我检查", "继续优化", "再优化", "复盘"),
        state_schema=("iteration", "stable_brief", "draft_prompt", "critique", "revision_delta", "quality_score"),
        critique_axes=("intent_fit", "specificity", "constraint_compliance", "text_accuracy", "prompt_executability"),
        revision_axes=("brief_boundary", "composition", "style_precision", "text_policy", "negative_controls"),
        stop_conditions=("quality_score >= 0.88", "no material revision_delta", "max_iterations reached"),
        next_prompt_template=(
            "Use the stable brief and previous critique to rewrite only the weakest prompt axis. "
            "Return: revised prompt, changed axis, reason, remaining risk, quality score."
        ),
        negative_controls=("do not rewrite the user's goal", "do not add unrelated style", "do not expand constraints without evidence"),
    ),
    "design_critic_loop": LoopProfile(
        loop_type="design_critic_loop",
        title="Design critic revision loop",
        purpose="Improve visual design prompts through repeated aesthetic critique and controlled revision.",
        triggers=("审美", "画面", "排版", "构图", "细碎", "脏乱", "秩序", "文字精准", "乱码", "设计感"),
        state_schema=("iteration", "visual_goal", "dominant_anchor", "layout_grid", "critic_findings", "revision_delta"),
        critique_axes=("dominant_anchor", "layout_order", "density_ceiling", "color_control", "typography", "anti_fragmentation"),
        revision_axes=("focal_hierarchy", "grid", "negative_space", "palette", "type_hierarchy", "visible_text"),
        stop_conditions=("no critical aesthetic finding", "density and text gates pass", "max_iterations reached"),
        next_prompt_template=(
            "Revise the visual prompt by strengthening one dominant anchor, one grid rule, and one density limit. "
            "Keep visible text exact and remove decorative clutter."
        ),
        negative_controls=("no random icons", "no noisy texture", "no pseudo-Chinese", "no overlapping labels", "no dirty background debris"),
    ),
    "failure_memory_loop": LoopProfile(
        loop_type="failure_memory_loop",
        title="Failure-memory recovery loop",
        purpose="Convert rejected or failed outputs into explicit failure modes and safer next prompts.",
        triggers=("失败", "不成功", "不算数", "当做没发生", "好丑", "不好", "跑偏", "崩了", "重来"),
        state_schema=("iteration", "observed_failure", "failure_mode", "root_cause", "locked_elements", "next_prompt"),
        critique_axes=("root_cause", "locked_elements", "drift_source", "missing_constraint", "overconstraint"),
        revision_axes=("failure_mode", "must_not_repeat", "source_lock", "next_attempt_boundary", "qa_gate"),
        stop_conditions=("failure_mode resolved", "same failure repeats twice", "user accepts direction"),
        next_prompt_template=(
            "Name the failure mode first, then write the next prompt with explicit locks and must-not-repeat controls. "
            "Do not preserve the failed aesthetic unless the user asks."
        ),
        negative_controls=("do not defend the failed result", "do not repeat rejected style", "do not hide uncertainty"),
    ),
    "branch_search_loop": LoopProfile(
        loop_type="branch_search_loop",
        title="Branch search prompt loop",
        purpose="Explore several prompt directions, score them, and recombine the best parts into a stronger next prompt.",
        triggers=("多方案", "方向", "分支", "branch", "探索", "候选", "三版", "多版", "方案比较"),
        state_schema=("iteration", "branches", "branch_scores", "winning_parts", "recombined_prompt", "discarded_parts"),
        critique_axes=("novelty", "domain_fit", "constraint_fit", "aesthetic_potential", "risk_control"),
        revision_axes=("branch_thesis", "composition_logic", "style_axis", "evidence_support", "risk_boundary"),
        stop_conditions=("one branch dominates by score margin >= 0.12", "recombined prompt passes critic", "max_iterations reached"),
        next_prompt_template=(
            "Generate 3 branches that vary only one strategic dimension. Score each branch, keep the best parts, "
            "and produce one recombined prompt."
        ),
        negative_controls=("do not mix incompatible contexts", "do not average all styles", "do not make every branch decorative"),
    ),
    "visual_result_loop": LoopProfile(
        loop_type="visual_result_loop",
        title="Visual-result repair loop",
        purpose="Diagnose an image or generated result, preserve what works, and produce a targeted edit or regeneration prompt.",
        triggers=("改图", "修图", "结果", "优化这张", "拯救", "继续修", "不要改变", "保留", "参考图"),
        state_schema=("iteration", "source_image_locks", "observed_result", "change_only", "preserve", "next_edit_prompt"),
        critique_axes=("identity_or_object_lock", "composition", "lighting", "texture", "geometry", "text_or_label_integrity"),
        revision_axes=("local_edit_region", "preservation_rule", "blend_rule", "crop_or_layout", "color_grade"),
        stop_conditions=("locked elements remain stable", "target defect removed", "no new artifacts"),
        next_prompt_template=(
            "Write an edit prompt that starts with preservation locks, then states change-only regions, blending rules, "
            "and artifact controls."
        ),
        negative_controls=("no identity drift", "no face replacement", "no warped product edges", "no fake labels", "no over-retouching"),
    ),
    "seamless_video_loop": LoopProfile(
        loop_type="seamless_video_loop",
        title="Seamless video loop prompt",
        purpose="Create video or motion prompts where the first and last frames connect without a visible jump.",
        triggers=("无缝循环", "首尾", "循环视频", "loop video", "seamless", "动效", "镜头循环", "首尾一致"),
        state_schema=("iteration", "first_frame", "last_frame", "motion_period", "camera_path", "loop_closure", "temporal_artifacts"),
        critique_axes=("first_last_consistency", "motion_continuity", "camera_path_closure", "lighting_continuity", "subject_continuity"),
        revision_axes=("periodic_motion", "closed_camera_path", "stable_subject_state", "repeatable_particles", "temporal_negative_prompt"),
        stop_conditions=("first and last frame match", "no pop or cut", "motion period is visually periodic"),
        next_prompt_template=(
            "Write a video prompt with a closed camera path and periodic motion. Define first frame, last frame, "
            "loop duration, and temporal negative controls."
        ),
        negative_controls=("no scene cut", "no camera snap", "no object popping", "no morphing", "no flicker", "no text drift"),
    ),
}


class LoopPromptPackBuilder:
    """Independent companion prompt system for iterative and loop-based prompting."""

    DEFAULT_MAX_ITERATIONS = 3

    @classmethod
    def should_activate_text(cls, text):
        return cls().detect(text).active

    def detect(self, text, intent=None, route=None):
        raw = str(text or "")
        lowered = raw.lower()
        intent_domains = tuple(getattr(intent, "domains", ()) or ())
        delivery_modes = tuple(getattr(intent, "delivery_modes", ()) or ())
        route_skill = (route or {}).get("skill_name", "")
        score_table = {}
        trigger_hits = []
        for loop_type, profile in LOOP_PROFILES.items():
            hits = tuple(keyword for keyword in profile.triggers if keyword.lower() in lowered)
            score = float(len(hits))
            if loop_type == "seamless_video_loop" and ("short-video-aigc" in intent_domains or route_skill == "ShortDramaAIGC_OS"):
                score += 1.2
            if loop_type == "visual_result_loop" and ("image_edit" in delivery_modes or "photography" in intent_domains):
                score += 0.9
            if loop_type == "design_critic_loop" and any(risk in getattr(intent, "risks", ()) for risk in ("fragmented_visual", "text_error_or_mojibake")):
                score += 0.8
            score_table[loop_type] = {"score": round(score, 4), "hits": hits}
            trigger_hits.extend(hits)

        ranked = sorted(score_table.items(), key=lambda item: (-item[1]["score"], item[0]))
        winner, winner_data = ranked[0]
        best_score = winner_data["score"]
        second_score = ranked[1][1]["score"] if len(ranked) > 1 else 0.0
        active = best_score > 0
        confidence = 0.0
        if active:
            confidence = min(0.98, 0.48 + best_score * 0.12 + max(0.0, best_score - second_score) * 0.08)
        return LoopDetection(
            active=active,
            loop_type=winner if active else "inactive",
            confidence=round(confidence, 4),
            trigger_hits=tuple(dict.fromkeys(trigger_hits)),
            score_table=score_table,
        )

    def build(
        self,
        text,
        intent=None,
        route=None,
        genome=None,
        memory=None,
        candidates=None,
        critics=None,
        constraints=None,
        failure_memory=None,
    ):
        detection = self.detect(text, intent=intent, route=route)
        profile = LOOP_PROFILES.get(detection.loop_type, LOOP_PROFILES["self_refine_loop"])
        pack = {
            "schema_version": LOOP_PROMPT_PACK_VERSION,
            "packet_type": "LoopPromptPack",
            "relationship_to_prompt_packet_v2": {
                "mode": "independent_companion_pack",
                "does_not_replace_prompt_packet_v2": True,
                "activation": "active" if detection.active else "available_but_inactive",
                "use_policy": "Call this pack only when iterative prompting, failed-result recovery, branch exploration, or seamless motion loops are needed.",
            },
            "task_brief": str(text or ""),
            "activation": detection.to_dict(),
            "loop_contract": self._loop_contract(profile, detection),
            "context_snapshot": self._context_snapshot(intent, route, genome, memory, candidates, critics, constraints, failure_memory),
            "stage_prompts": self._stage_prompts(profile),
            "quality_gate": self._quality_gate(profile),
            "export_policy": {
                "can_be_saved_as_standalone_json": True,
                "can_be_attached_to_prompt_packet_v2": True,
                "write_failure_memory_after_rejection": profile.loop_type in ("failure_memory_loop", "visual_result_loop", "design_critic_loop"),
            },
        }
        return pack

    def _loop_contract(self, profile, detection):
        return {
            "loop_type": profile.loop_type if detection.active else "select_on_demand",
            "title": profile.title,
            "purpose": profile.purpose,
            "max_iterations": self.DEFAULT_MAX_ITERATIONS,
            "state_schema": profile.state_schema,
            "critique_axes": profile.critique_axes,
            "revision_axes": profile.revision_axes,
            "stop_conditions": profile.stop_conditions,
            "next_prompt_template": profile.next_prompt_template,
            "negative_controls": profile.negative_controls,
        }

    def _context_snapshot(self, intent, route, genome, memory, candidates, critics, constraints, failure_memory):
        top_candidates = []
        for candidate in (candidates or [])[:3]:
            top_candidates.append({
                "id": candidate.get("id"),
                "thesis": candidate.get("thesis"),
                "final_score": candidate.get("final_score"),
                "risk_to_watch": candidate.get("risk_to_watch"),
            })
        memory_items = []
        for item in (memory or {}).get("results", [])[:3]:
            memory_items.append({
                "case_id": item.get("case_id"),
                "title": item.get("title"),
                "memory_score": item.get("memory_score"),
                "role": item.get("style_axis"),
            })
        return {
            "intent": asdict(intent) if hasattr(intent, "__dataclass_fields__") else {},
            "route_skill": (route or {}).get("skill_name", ""),
            "aesthetic_genome": genome or {},
            "memory_refs": memory_items,
            "top_candidate_refs": top_candidates,
            "hard_constraints": (constraints or {}).get("hard_constraints", ()),
            "risk_controls": (constraints or {}).get("risk_controls", ()),
            "active_failure_modes": (failure_memory or {}).get("active_failure_modes", ()),
            "critic_summary": [critic for critic in (critics or []) if critic.get("critic") in ("KernelAggregateCritic", "AestheticCritic", "ConstraintCritic")],
        }

    def _stage_prompts(self, profile):
        return {
            "loop_controller_prompt": (
                "You are the LoopPromptPack controller. Keep the user's original brief stable. "
                "Run one iteration at a time. Each iteration must output state, critique, revision_delta, "
                "revised_prompt, score, and stop_or_continue."
            ),
            "draft_prompt": (
                "Draft a production-ready prompt from the stable brief. Preserve hard constraints. "
                "Make the result concrete enough to execute in one model/tool."
            ),
            "critique_prompt": (
                "Critique the current prompt using these axes: "
                + ", ".join(profile.critique_axes)
                + ". Name only actionable defects."
            ),
            "revision_prompt": profile.next_prompt_template,
            "stop_check_prompt": (
                "Check stop conditions: "
                + "; ".join(profile.stop_conditions)
                + ". If not satisfied, name the single next revision axis."
            ),
        }

    def _quality_gate(self, profile):
        return {
            "must_pass": (
                "stable original brief",
                "one changed axis per iteration",
                "explicit preservation locks",
                "measurable critique score",
                "clear stop condition",
            ),
            "loop_specific_axes": profile.critique_axes,
            "negative_controls": profile.negative_controls,
        }
