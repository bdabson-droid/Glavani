#!/usr/bin/env bash
# Build site and push to gh-pages branch for GitHub Pages preview.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEPLOY_DIR="/tmp/gh-pages-deploy-$$"
trap 'rm -rf "$DEPLOY_DIR"' EXIT

cd "$ROOT"
python3 scripts/build_site.py

git fetch origin gh-pages
git worktree add "$DEPLOY_DIR" origin/gh-pages

rm -rf "$DEPLOY_DIR"/{assets,en,hr,images}
cp -r "$ROOT"/{assets,en,hr,images} "$DEPLOY_DIR"/
cp "$ROOT"/{index.html,robots.txt,sitemap.xml,manifest.webmanifest} "$DEPLOY_DIR"/
touch "$DEPLOY_DIR/.nojekyll"

cd "$DEPLOY_DIR"
git add -A
if git diff --cached --quiet; then
  echo "No gh-pages changes to deploy."
else
  git commit -m "${1:-Deploy site to GitHub Pages}"
  git push origin HEAD:gh-pages
fi
