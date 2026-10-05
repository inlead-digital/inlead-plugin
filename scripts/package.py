"""Builds the upload packages in dist/ after checking that every manifest carries the same version."""

import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "inlead"
DIST = ROOT / "dist"

MANIFESTS = [
    PLUGIN / ".claude-plugin" / "plugin.json",
    PLUGIN / ".cursor-plugin" / "plugin.json",
    PLUGIN / "plugin.json",
]

# The OpenAI package must carry mcp.json: OpenAI can't add an MCP server to a skills-only plugin later.
PACKAGES = {
    "claude": [".claude-plugin", ".mcp.json", "README.md", "skills"],
    "openai": ["plugin.json", "mcp.json", "README.md", "assets", "skills"],
}

IGNORED = {".DS_Store", "Thumbs.db", "desktop.ini"}


def read_versions() -> dict[str, str]:
    versions = {str(path.relative_to(ROOT)): json.loads(path.read_text())["version"] for path in MANIFESTS}
    marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    for entry in marketplace["plugins"]:
        if entry["name"] == "inlead":
            versions[".claude-plugin/marketplace.json"] = entry["version"]
    return versions


def build(name: str, entries: list[str], version: str) -> Path:
    target = DIST / f"inlead-{name}-{version}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for entry in entries:
            source = PLUGIN / entry
            files = [source] if source.is_file() else sorted(p for p in source.rglob("*") if p.is_file())
            for file in files:
                if file.name not in IGNORED:
                    archive.write(file, file.relative_to(PLUGIN).as_posix())
    return target


def main() -> None:
    versions = read_versions()
    if len(set(versions.values())) != 1:
        sys.exit("Version mismatch:\n" + "\n".join(f"  {path}: {version}" for path, version in versions.items()))

    version = next(iter(versions.values()))
    DIST.mkdir(exist_ok=True)
    for name, entries in PACKAGES.items():
        print(build(name, entries, version).relative_to(ROOT))


if __name__ == "__main__":
    main()
