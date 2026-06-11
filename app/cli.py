import argparse
import json
from app.core.aesthetic_quality import AestheticQualityGate
from app.core.design_kernel import DesignKernel, FailureMemoryBank
from app.core.capabilities import capability_report
from app.core.envart_cadmcp import EnvArtCADMCPBridge
from app.core.orchestrator import MasterOrchestrator
from app.lora_training.aesthetic_memory import AestheticMemoryIndex
from app.lora_training.aesthetic_space import LoRAAestheticSpace
from app.lora_training.service import LoRAStyleTrainingLibrary
from app.management.git_ops_manager import GitOpsManager
from app.management.github_manager import GitHubManager
from app.management.skill_registry_sync import SkillRegistrySyncAgent

def json_dumps(payload):
    return json.dumps(payload, ensure_ascii=False, indent=2)

def main():
    parser = argparse.ArgumentParser(prog="designosforge")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("capabilities")
    run_parser = sub.add_parser("run")
    run_parser.add_argument("prompt")
    run_parser.add_argument("--confirm-image-generation", action="store_true")
    run_parser.add_argument("--prompt-packet", action="store_true")
    lora_parser = sub.add_parser("lora")
    lora_parser.add_argument("action", choices=("status", "init", "init-aesthetic-space", "audit-corpus", "build-memory-index", "recommend"))
    lora_parser.add_argument("--name", default="default-style-library")
    lora_parser.add_argument("--style-token", default="<designosforge_style>")
    lora_parser.add_argument("--root", default="lora_training_sandbox/aesthetic_corpus")
    lora_parser.add_argument("--taxonomy", default="config/lora_training/aesthetic_taxonomy.json")
    lora_parser.add_argument("--domain", default="")
    lora_parser.add_argument("--context", default="")
    lora_parser.add_argument("--style-axis", default="")
    lora_parser.add_argument("--limit", type=int, default=5)
    gitops_parser = sub.add_parser("gitops")
    gitops_parser.add_argument("action", choices=("status", "diff", "sync-registry"))
    gitops_parser.add_argument("--repo", default=".")
    github_parser = sub.add_parser("github")
    github_parser.add_argument("action", choices=("status", "release-plan", "pr-template"))
    github_parser.add_argument("--repo", default=".")
    github_parser.add_argument("--version", default="v2.0.0")
    quality_parser = sub.add_parser("quality")
    quality_parser.add_argument("action", choices=("audit", "guardrails"))
    quality_parser.add_argument("text")
    envart_cad_parser = sub.add_parser("envart-cad")
    envart_cad_parser.add_argument("action", choices=("plan",))
    envart_cad_parser.add_argument("text")
    kernel_parser = sub.add_parser("kernel")
    kernel_parser.add_argument("action", choices=("plan", "prompt-packet", "loop-prompt", "math-audit", "record-failure"))
    kernel_parser.add_argument("text")
    kernel_parser.add_argument("--domain", default="general-design")
    kernel_parser.add_argument("--failure-mode", default="unspecified_failure")
    kernel_parser.add_argument("--note", default="")
    args = parser.parse_args()
    if args.command == "capabilities":
        print(capability_report())
    elif args.command == "run":
        print(MasterOrchestrator().run(args.prompt, args.confirm_image_generation, args.prompt_packet))
    elif args.command == "lora":
        if args.action == "init-aesthetic-space":
            print(LoRAAestheticSpace(args.root, args.taxonomy).init_space())
        elif args.action == "audit-corpus":
            print(json_dumps(AestheticMemoryIndex(args.root).audit()))
        elif args.action == "build-memory-index":
            print(json_dumps(AestheticMemoryIndex(args.root).build_index()))
        elif args.action == "recommend":
            memory = AestheticMemoryIndex(args.root)
            print(json_dumps(memory.recommend(args.domain, args.context, args.style_axis, args.limit)))
        else:
            service = LoRAStyleTrainingLibrary()
            print(service.status() if args.action == "status" else service.init_library(args.name, args.style_token))
    elif args.command == "gitops":
        print(SkillRegistrySyncAgent(args.repo).report() if args.action == "sync-registry" else (GitOpsManager(args.repo).status() if args.action == "status" else GitOpsManager(args.repo).diff()))
    elif args.command == "github":
        manager = GitHubManager(args.repo)
        if args.action == "status":
            print(manager.status())
        elif args.action == "release-plan":
            print(manager.release_plan(args.version))
        else:
            print(manager.pr_template(args.version))
    elif args.command == "quality":
        gate = AestheticQualityGate()
        print(gate.audit_json(args.text) if args.action == "audit" else gate.guardrail_text(args.text))
    elif args.command == "envart-cad":
        print(EnvArtCADMCPBridge().plan(args.text).to_json())
    elif args.command == "kernel":
        if args.action == "record-failure":
            print(json_dumps(FailureMemoryBank().record(args.text, args.domain, args.failure_mode, args.note)))
        else:
            plan = DesignKernel().plan(args.text).to_dict()
            if args.action == "prompt-packet":
                print(json_dumps(plan["prompt_packet_v2"]))
            elif args.action == "loop-prompt":
                print(json_dumps(plan["loop_prompt_pack"]))
            elif args.action == "math-audit":
                print(json_dumps(plan["math_trace"]))
            else:
                print(json_dumps(plan))

if __name__ == "__main__":
    main()
