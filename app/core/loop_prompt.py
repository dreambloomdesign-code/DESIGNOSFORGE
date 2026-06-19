from dataclasses import asdict, dataclass


LOOP_PROMPT_PACK_VERSION = "2.1.0-loop.1"
LOOP_ENGINEERING_VERSION = "2.1.0-loop-engineering.1"


LOOP_ENGINEERING_TRIGGERS = (
    "loop engineering",
    "loop-engineering",
    "agent loop",
    "autonomous loop",
    "scheduler",
    "schedule",
    "event trigger",
    "trigger",
    "parallel",
    "multi-agent",
    "multiple agents",
    "worktree",
    "isolation",
    "skill",
    "project knowledge",
    "connector",
    "external system",
    "issue",
    "ci",
    "pr",
    "acceptance",
    "validation",
    "validator",
    "verifier",
    "review",
    "memory",
    "persistent memory",
    "long-running loop",
    "\u8c03\u5ea6",
    "\u5b9a\u65f6",
    "\u4e8b\u4ef6\u89e6\u53d1",
    "\u89e6\u53d1",
    "\u5e76\u884c",
    "\u591a\u4e2a agent",
    "\u9694\u79bb",
    "\u9879\u76ee\u77e5\u8bc6",
    "\u8fde\u63a5\u5668",
    "\u5916\u90e8\u7cfb\u7edf",
    "\u9a8c\u6536",
    "\u9a8c\u8bc1",
    "\u8bb0\u5fc6",
    "\u957f\u671f loop",
    "\u8fd0\u884c\u7cfb\u7edf",
)


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


@dataclass(frozen=True)
class LoopEngineeringDetection:
    active: bool
    confidence: float
    trigger_hits: tuple[str, ...]
    runtime_mode: str

    def to_dict(self):
        return asdict(self)


LOOP_PROFILES = {
    "self_refine_loop": LoopProfile(
        loop_type="self_refine_loop",
        title="Self-refine prompt iteration",
        purpose="Draft, critique, revise, and rescore a prompt while keeping the original brief stable.",
        triggers=(
            "loop",
            "iteration",
            "self critique",
            "self-check",
            "refine",
            "continue optimizing",
            "\u5faa\u73af",
            "\u95ed\u73af",
            "\u8fed\u4ee3",
            "\u53cd\u590d",
            "\u591a\u8f6e",
            "\u81ea\u6211\u68c0\u67e5",
            "\u7ee7\u7eed\u4f18\u5316",
            "\u518d\u4f18\u5316",
            "\u590d\u76d8",
        ),
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
        triggers=(
            "aesthetic",
            "composition",
            "layout",
            "typography",
            "fragmented",
            "messy",
            "dirty",
            "text precision",
            "mojibake",
            "\u5ba1\u7f8e",
            "\u753b\u9762",
            "\u6392\u7248",
            "\u6784\u56fe",
            "\u7ec6\u788e",
            "\u810f\u4e71",
            "\u79e9\u5e8f",
            "\u6587\u5b57\u7cbe\u51c6",
            "\u4e71\u7801",
            "\u8bbe\u8ba1\u611f",
        ),
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
        triggers=(
            "failed",
            "failure",
            "not successful",
            "does not count",
            "ignore this result",
            "bad",
            "off target",
            "redo",
            "\u5931\u8d25",
            "\u4e0d\u6210\u529f",
            "\u4e0d\u7b97\u6570",
            "\u5f53\u505a\u6ca1\u53d1\u751f",
            "\u597d\u4e11",
            "\u4e0d\u597d",
            "\u8dd1\u504f",
            "\u5d29\u4e86",
            "\u91cd\u6765",
        ),
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
        triggers=(
            "branch",
            "multiple options",
            "directions",
            "explore",
            "candidate",
            "three versions",
            "compare options",
            "\u591a\u65b9\u6848",
            "\u65b9\u5411",
            "\u5206\u652f",
            "\u63a2\u7d22",
            "\u5019\u9009",
            "\u4e09\u7248",
            "\u591a\u7248",
            "\u65b9\u6848\u6bd4\u8f83",
        ),
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
        triggers=(
            "edit image",
            "retouch",
            "result",
            "optimize this image",
            "repair",
            "preserve",
            "do not change",
            "reference image",
            "\u6539\u56fe",
            "\u4fee\u56fe",
            "\u7ed3\u679c",
            "\u4f18\u5316\u8fd9\u5f20",
            "\u62ef\u6551",
            "\u7ee7\u7eed\u4fee",
            "\u4e0d\u8981\u6539\u53d8",
            "\u4fdd\u7559",
            "\u53c2\u8003\u56fe",
        ),
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
        triggers=(
            "loop video",
            "seamless",
            "first and last frame",
            "closed camera path",
            "motion loop",
            "\u65e0\u7f1d\u5faa\u73af",
            "\u9996\u5c3e",
            "\u5faa\u73af\u89c6\u9891",
            "\u52a8\u6548",
            "\u955c\u5934\u5faa\u73af",
            "\u9996\u5c3e\u4e00\u81f4",
        ),
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
        return {
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


class LoopEngineeringBlueprintBuilder:
    """System blueprint for long-running, tool-connected, memory-backed agent loops."""

    def detect(self, text, loop_detection=None):
        raw = str(text or "")
        lowered = raw.lower()
        hits = tuple(trigger for trigger in LOOP_ENGINEERING_TRIGGERS if trigger.lower() in lowered)
        loop_active = bool(getattr(loop_detection, "active", False))
        systemic_hits = sum(
            1
            for token in (
                "system",
                "engineering",
                "runtime",
                "autonomous",
                "long-running",
                "architecture",
                "\u7cfb\u7edf",
                "\u5de5\u7a0b",
                "\u8fd0\u884c",
                "\u81ea\u52a8",
                "\u957f\u671f",
                "\u67b6\u6784",
                "\u9769\u65b0",
            )
            if token in lowered or token in raw
        )
        score = len(hits) + systemic_hits * 0.4 + (0.8 if loop_active else 0.0)
        active = bool(hits) or score >= 1.2
        runtime_mode = self._runtime_mode(lowered, raw)
        confidence = 0.0 if not active else min(0.98, 0.52 + score * 0.08)
        return LoopEngineeringDetection(
            active=active,
            confidence=round(confidence, 4),
            trigger_hits=tuple(dict.fromkeys(hits)),
            runtime_mode=runtime_mode,
        )

    def build(self, text, intent=None, route=None, loop_detection=None, constraints=None, failure_memory=None):
        detection = self.detect(text, loop_detection=loop_detection)
        route_skill = (route or {}).get("skill_name", "")
        context = tuple(getattr(intent, "project_contexts", ()) or ())
        domains = tuple(getattr(intent, "domains", ()) or ())
        return {
            "schema_version": LOOP_ENGINEERING_VERSION,
            "packet_type": "LoopEngineeringBlueprint",
            "relationship_to_loop_prompt_pack": {
                "mode": "system_runtime_layer",
                "does_not_replace_loop_prompt_pack": True,
                "use_policy": (
                    "Use LoopPromptPack for prompt iteration. Use LoopEngineeringBlueprint when the loop must run as a "
                    "scheduled/event-driven, multi-agent, tool-connected, validated, persistent system."
                ),
            },
            "activation": detection.to_dict(),
            "six_question_contract": self._six_question_contract(),
            "runtime_blueprint": {
                "scheduler": self._scheduler(text, detection),
                "parallel_isolation": self._parallel_isolation(text),
                "skill_context": self._skill_context(route_skill, domains, context),
                "external_connectors": self._external_connectors(text, route_skill),
                "validation_gate": self._validation_gate(route_skill, constraints or {}),
                "persistent_memory": self._persistent_memory(failure_memory or {}),
            },
            "agent_topology": self._agent_topology(route_skill),
            "state_schema": self._state_schema(),
            "handoff_contract": self._handoff_contract(),
            "failure_controls": self._failure_controls(),
            "prompt_scaffold": self._prompt_scaffold(),
            "export_policy": {
                "can_be_saved_as_standalone_json": True,
                "can_be_attached_to_loop_prompt_pack": True,
                "recommended_memory_file": "docs/LOOP_STATE.md",
                "recommended_task_board": "GitHub Issues or local markdown board",
            },
        }

    def _runtime_mode(self, lowered, raw):
        if any(token in lowered for token in ("ci", "test", "issue", "pr", "github")):
            return "event_connected_dev_loop"
        if any(token in lowered or token in raw for token in ("design", "aesthetic", "visual", "prompt", "\u8bbe\u8ba1", "\u5ba1\u7f8e", "\u56fe", "\u89c6\u89c9", "\u63d0\u793a\u8bcd")):
            return "design_quality_loop"
        if any(token in lowered or token in raw for token in ("daily", "every day", "half hour", "30 minutes", "\u5b9a\u65f6", "\u6bcf\u5929", "\u6bcf\u534a\u5c0f\u65f6", "\u8c03\u5ea6")):
            return "scheduled_monitor_loop"
        return "general_agent_loop"

    def _six_question_contract(self):
        return (
            {
                "question": "who_wakes_the_loop",
                "engineering_layer": "scheduler",
                "must_answer": "manual trigger, cron interval, event trigger, test failure trigger, or goal-until-done trigger",
            },
            {
                "question": "how_parallel_agents_do_not_collide",
                "engineering_layer": "parallel_isolation",
                "must_answer": "worktree/sandbox per agent, ownership boundaries, merge policy, conflict gate",
            },
            {
                "question": "how_the_agent_knows_project_habits",
                "engineering_layer": "skill_context",
                "must_answer": "required skills, project rules, no-touch paths, naming conventions, known traps",
            },
            {
                "question": "what_external_systems_it_can_touch",
                "engineering_layer": "external_connectors",
                "must_answer": "issues, CI, tests, database, PR, notifications, local files, browser, CAD, image tools",
            },
            {
                "question": "who_validates_the_result",
                "engineering_layer": "validation_gate",
                "must_answer": "separate executor and verifier, tests, critics, human review threshold, rollback gate",
            },
            {
                "question": "how_it_remembers_yesterday",
                "engineering_layer": "persistent_memory",
                "must_answer": "state file, decisions, confirmed facts, failures, blocked items, next wake target",
            },
        )

    def _scheduler(self, text, detection):
        raw = str(text or "")
        lowered = raw.lower()
        if any(token in lowered or token in raw for token in ("daily", "every day", "yesterday", "\u6bcf\u5929", "\u6bcf\u65e5", "\u6628\u665a")):
            trigger = "cron_daily"
            cadence = "once_per_day"
        elif any(token in lowered or token in raw for token in ("half hour", "30 minutes", "30\u5206\u949f", "\u534a\u5c0f\u65f6", "\u6bcf\u534a\u5c0f\u65f6")):
            trigger = "cron_interval"
            cadence = "30_minutes"
        elif any(token in lowered for token in ("ci", "issue", "pr", "test", "event")):
            trigger = "event_trigger"
            cadence = "on_external_event"
        elif detection.active:
            trigger = "goal_until_done"
            cadence = "iterate_until_stop_condition"
        else:
            trigger = "manual"
            cadence = "user_invoked"
        return {
            "trigger_type": trigger,
            "cadence": cadence,
            "wake_conditions": (
                "new user request",
                "external event arrives",
                "validation fails",
                "scheduled time reached",
                "open task remains incomplete",
            ),
            "stop_conditions": (
                "acceptance gates pass",
                "same blocker repeats three times",
                "human review required",
                "budget or safety boundary reached",
            ),
        }

    def _parallel_isolation(self, text):
        lowered = str(text or "").lower()
        needs_parallel = any(token in lowered for token in ("parallel", "multi-agent", "multiple agents", "worktree", "\u5e76\u884c", "\u591a\u4e2a agent"))
        return {
            "isolation_mode": "git_worktree_per_agent" if needs_parallel else "single_workspace_with_file_ownership",
            "workspace_rule": "Each executor gets its own branch/worktree when edits may overlap.",
            "ownership_policy": (
                "declare touched paths before edit",
                "never rewrite files owned by another active agent",
                "merge through review, not direct overwrite",
            ),
            "conflict_gate": "run diff, tests, and reviewer check before merging agent outputs",
        }

    def _skill_context(self, route_skill, domains, context):
        skill_refs = ["designos-forge"]
        if route_skill:
            skill_refs.append(route_skill)
        if "spatial-cad-production" in context or "environmental-art" in domains:
            skill_refs.append("cad-drawing-control")
        if "photography" in domains:
            skill_refs.append("PhotographyOS")
        return {
            "required_skill_refs": tuple(dict.fromkeys(skill_refs)),
            "project_knowledge_sources": (
                "codex_skill/designos-forge/SKILL.md",
                "docs/LOOP_PROMPT_PACK.md",
                "docs/LOOP_ENGINEERING.md",
                "lora_training_sandbox/aesthetic_corpus/aesthetic_memory_index.json",
            ),
            "long_term_rules": (
                "respect no-touch directories and user changes",
                "route by project context before visual style",
                "write rejected patterns into failure memory",
                "keep visible text exact and UTF-8 safe",
            ),
        }

    def _external_connectors(self, text, route_skill):
        lowered = str(text or "").lower()
        connectors = ["local_files", "git"]
        if any(token in lowered for token in ("github", "issue", "pr", "ci")):
            connectors.extend(["github_issues", "github_actions", "pull_requests"])
        if "browser" in lowered or route_skill in ("WebDesignOS", "UIDesignSpecOS"):
            connectors.append("browser_qa")
        if route_skill == "EnvArtCADMCPBridge":
            connectors.append("cad_mcp")
        if route_skill == "PhotographyOS":
            connectors.append("image_editing")
        return {
            "connectors": tuple(dict.fromkeys(connectors)),
            "tool_boundary": "Prefer deterministic local tools and official connectors; record every external side effect.",
            "side_effect_policy": (
                "read before write",
                "commit or log durable changes",
                "do not publish or notify without explicit user intent",
            ),
        }

    def _validation_gate(self, route_skill, constraints):
        validators = ["self_check", "independent_critic", "git_diff_check"]
        if route_skill == "EnvArtCADMCPBridge":
            validators.extend(["cad_health", "dxf_audit", "geometry_lock_check"])
        if route_skill == "PhotographyOS":
            validators.extend(["identity_preservation_check", "artifact_check"])
        if route_skill in ("InfoVisOS", "LayeredBoardComposer", "PosterDesignOS"):
            validators.extend(["layout_order_check", "text_accuracy_check"])
        return {
            "executor_validator_split": True,
            "validators": tuple(dict.fromkeys(validators)),
            "acceptance_thresholds": {
                "tests_or_audit": "pass",
                "constraint_satisfaction": (constraints.get("penalty_vector", {}) or {}).get("constraint_satisfaction", ">=0.88"),
                "no_repeated_failure": True,
                "human_review_required_if": "external side effects, ambiguous source truth, destructive edit, or low confidence",
            },
        }

    def _persistent_memory(self, failure_memory):
        return {
            "memory_files": (
                "docs/LOOP_STATE.md",
                "lora_training_sandbox/aesthetic_corpus/failure_memory.jsonl",
                "delivery manifest or PR body",
            ),
            "write_after_each_iteration": (
                "current_goal",
                "files_touched",
                "validation_result",
                "decision_log",
                "failure_modes",
                "next_wake_condition",
            ),
            "known_failure_count": failure_memory.get("total_items", 0),
            "principle": "The model may forget, but the repository must not.",
        }

    def _agent_topology(self, route_skill):
        return {
            "roles": (
                {"name": "scheduler", "responsibility": "wake loop and decide whether work continues"},
                {"name": "executor", "responsibility": f"perform route-specific work through {route_skill or 'selected route'}"},
                {"name": "verifier", "responsibility": "run tests, audits, critic checks, and acceptance gates"},
                {"name": "memory_writer", "responsibility": "persist state, failures, and handoff notes"},
                {"name": "merge_or_handoff", "responsibility": "merge accepted work or ask human review"},
            ),
            "recommended_parallelism": "parallel branches only when isolated by worktree and path ownership",
        }

    def _state_schema(self):
        return {
            "loop_id": "stable identifier",
            "iteration": "integer",
            "wake_reason": "manual | schedule | event | validation_failure | open_goal",
            "assigned_agent": "executor/verifier/memory_writer",
            "workspace": "main workspace or worktree path",
            "input_snapshot": "brief, issue, CI log, file set, or source assets",
            "action_plan": "single-iteration plan",
            "side_effects": "files, branches, PRs, notifications, external records",
            "validation_result": "pass/fail/needs_human",
            "memory_delta": "new facts, failures, decisions, next wake condition",
        }

    def _handoff_contract(self):
        return {
            "human_handoff_when": (
                "validator cannot prove correctness",
                "same blocker repeats",
                "external permission is missing",
                "merge conflict requires product judgment",
                "visual or cultural judgment is ambiguous",
            ),
            "handoff_payload": (
                "goal",
                "current state",
                "what was tried",
                "validation evidence",
                "remaining decision",
                "safe next command",
            ),
        }

    def _failure_controls(self):
        return (
            "Do not let the executor validate itself as the only reviewer.",
            "Do not run parallel edits without workspace isolation.",
            "Do not loop indefinitely; every loop needs a stop rule.",
            "Do not re-open rejected directions without memory evidence.",
            "Do not touch external systems without a side-effect log.",
        )

    def _prompt_scaffold(self):
        return {
            "system_prompt": (
                "You are a Loop Engineering controller. Before acting, answer: trigger, isolation, skill context, "
                "external connectors, validation, persistent memory. Run one iteration, validate independently, "
                "then write state and stop/continue."
            ),
            "iteration_output_format": (
                "wake_reason, isolated_workspace, selected_skill_context, planned_side_effects, executor_actions, "
                "verifier_checks, memory_delta, stop_or_continue, next_wake_condition"
            ),
        }
