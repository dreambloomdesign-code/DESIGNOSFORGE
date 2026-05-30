from pathlib import Path
import re
import sys


SKILL_NAME = "designos-forge"


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    skill_md = root / "codex_skill" / SKILL_NAME / "SKILL.md"
    if not skill_md.exists():
        print(f"missing {skill_md}")
        return 1

    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        print("missing YAML frontmatter")
        return 1

    match = re.match(r"---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        print("malformed YAML frontmatter")
        return 1

    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()

    if fields.get("name") != SKILL_NAME:
        print("invalid skill name")
        return 1
    if not fields.get("description"):
        print("missing description")
        return 1
    if not re.fullmatch(r"[a-z0-9-]+", fields["name"]):
        print("skill name must be hyphen-case")
        return 1
    if "v1.5" not in text or "PromptPacket v1.5" not in text:
        print("v1.5 governance text missing")
        return 1

    print("source skill is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
