import json
import shutil
import subprocess
from pathlib import Path


class GitHubManager:
    def __init__(self, repo="."):
        self.repo = Path(repo)

    def _run(self, command):
        result = subprocess.run(
            command,
            cwd=self.repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        return result.returncode, result.stdout.strip()

    def _git(self, *args):
        return self._run(["git", *args])

    def _is_git_repo(self):
        code, output = self._git("rev-parse", "--is-inside-work-tree")
        return code == 0 and output.lower() == "true"

    def _branch(self):
        code, output = self._git("branch", "--show-current")
        return output if code == 0 else ""

    def _remotes(self):
        code, output = self._git("remote", "-v")
        if code != 0 or not output:
            return []
        rows = []
        for line in output.splitlines():
            parts = line.split()
            if len(parts) >= 3:
                rows.append({"name": parts[0], "url": parts[1], "mode": parts[2].strip("()")})
        return rows

    def _latest_tag(self):
        code, output = self._git("describe", "--tags", "--abbrev=0")
        return output if code == 0 else ""

    def status(self):
        is_repo = self._is_git_repo()
        status_code, status_output = self._git("status", "--short")
        payload = {
            "repo": str(self.repo),
            "is_git_repo": is_repo,
            "branch": self._branch() if is_repo else "",
            "remotes": self._remotes() if is_repo else [],
            "dirty_file_count": len(status_output.splitlines()) if status_code == 0 and status_output else 0,
            "latest_tag": self._latest_tag() if is_repo else "",
            "gh_available": shutil.which("gh") is not None,
            "recommended_next_action": self._recommendation(is_repo),
        }
        return json.dumps(payload, ensure_ascii=False, indent=2)

    def release_plan(self, version="v1.5.1"):
        branch = f"release/{version.lstrip('v')}"
        lines = [
            f"# DESIGNOSFORGE {version} GitHub Release Plan",
            "",
            "1. Confirm the working tree is clean or intentionally staged.",
            f"2. Create a release branch: `git switch -c {branch}`.",
            "3. Update skill metadata, source package version, README notes, and tests.",
            "4. Run validation: skill quick_validate, source CLI smoke checks, and pytest.",
            f"5. Commit with: `release: designosforge {version}`.",
            f"6. Tag with: `git tag {version}` after tests pass.",
            "7. Push branch and tag to GitHub.",
            "8. Open a draft PR with summary, validation evidence, migration notes, and rollback plan.",
            "9. Merge only after CI and review pass; publish a GitHub Release from the tag.",
        ]
        return "\n".join(lines)

    def pr_template(self, version="v1.5.1"):
        return "\n".join([
            f"# Release DESIGNOSFORGE {version}",
            "",
            "## Summary",
            "- Add v1.5 aesthetic quality, prompt precision, layout order, text accuracy, encoding, and redundancy gates.",
            "- Preserve DESIGNOSFORGE inference, GitHub management, and image confirmation gates.",
            "",
            "## Validation",
            "- [ ] Skill quick_validate passed",
            "- [ ] Source CLI smoke checks passed",
            "- [ ] pytest passed",
            "- [ ] GitHub branch, tag, and release notes checked",
            "",
            "## Rollback",
            "- Revert the release commit or restore the previous tag.",
        ])

    def _recommendation(self, is_repo):
        if not is_repo:
            return "Initialize git, make an initial commit, add a GitHub remote, then push a release branch."
        if not self._remotes():
            return "Add a GitHub remote named origin before PR or release workflows."
        return "Use branch, commit, push, draft PR, CI, tag, and GitHub Release workflow."
