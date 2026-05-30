# GitHub Publish Checklist

1. Confirm target repository owner/name.
2. Confirm the repository is public and MIT-licensed.
3. Add remote:

```bash
git remote add origin https://github.com/<owner>/<repo>.git
```

4. Push branch and tag:

```bash
git push -u origin release/1.5.0
git push origin v1.5.0
```

5. Open a draft PR using `docs/PR_BODY_v1.5.0.md`.
6. Wait for `.github/workflows/validate.yml` to pass.
7. Merge to `main`.
8. Publish GitHub Release `v1.5.0` using `docs/RELEASE_NOTES_v1.5.0.md`.
9. Keep `DESIGNOSFORGE_v1.5.0_git.bundle` as offline backup until remote is confirmed.
