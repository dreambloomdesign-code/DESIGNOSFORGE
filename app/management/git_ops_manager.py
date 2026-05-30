import subprocess
from pathlib import Path

class GitOpsManager:
    def __init__(self, repo="."):
        self.repo = Path(repo)
    def _git(self, *args):
        result = subprocess.run(["git", *args], cwd=self.repo, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
        return result.stdout.strip()
    def status(self):
        return self._git("status", "--short")
    def diff(self):
        return self._git("diff", "--stat")
    def checkpoint(self, message):
        self._git("add", ".")
        return self._git("commit", "-m", message)
    def tag(self, version):
        return self._git("tag", version)
