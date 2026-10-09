#!/usr/bin/env bash
set -euo pipefail
repo="${1:?Usage: bash scripts/publish-template.sh OWNER/NAME [private|public]}"
visibility="${2:-private}"
[[ "$repo" =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]] || { echo "Invalid OWNER/NAME" >&2; exit 1; }
[[ "$visibility" == private || "$visibility" == public ]] || { echo "Visibility must be private or public" >&2; exit 1; }
cd "$(dirname "$0")/.."
for tool in git gh python3; do command -v "$tool" >/dev/null || { echo "Missing $tool" >&2; exit 1; }; done
gh auth status
python3 scripts/validate.py
if git rev-parse --show-toplevel >/dev/null 2>&1; then
 [[ "$(git rev-parse --show-toplevel)" == "$(pwd -P)" ]] || { echo "Refusing nested checkout" >&2; exit 1; }
else
 git init -b main
fi
if git remote get-url origin >/dev/null 2>&1; then echo "Origin already exists; refusing creation" >&2; exit 1; fi
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
 git add .
 git commit -m "Initialize TISE Master Document repository template"
fi
gh repo create "$repo" "--$visibility" --source=. --remote=origin --push --description "TISE: the evolving story of a co-produced Master Document"
gh repo edit "$repo" --template
gh repo view "$repo" --json url,isTemplate --jq 'if .isTemplate then .url else error("Template flag not enabled") end'
