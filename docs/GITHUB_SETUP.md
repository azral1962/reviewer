# Publish as a GitHub template

This package is ready to publish but is not itself a live GitHub repository. With Python 3, Git and authenticated GitHub CLI installed, run from this directory:

```bash
bash scripts/publish-template.sh azral1962/tise-repository-template private
```

The script validates, creates an initial commit when needed, creates a new private repository, pushes it, enables its template setting and verifies that setting. It refuses an existing origin or a nested Git checkout. Pass `public` explicitly if you want a public template. Existing repositories are not overwritten.

Alternatively create an empty repository on GitHub, upload the package contents including `.github/`, then select **Settings → General → Template repository**. Add branch review rules appropriate to your project; the package does not configure server-side enforcement.

After publishing, choose **Use this template → Create a new repository** for each application. Template copies start a new Git history, so retain cycle records if the scholarly story must transfer.

For Codex: open the generated repository in VS Code, let Codex read root `AGENTS.md`, and explicitly supply the selected role prompt and cycle ID. No API key or external model runtime is needed for this document-based workflow.

Sources:
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository
- https://cli.github.com/manual/gh_repo_create
- https://cli.github.com/manual/gh_repo_edit
- https://learn.chatgpt.com/docs/agent-configuration/agents-md
