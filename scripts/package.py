"""Synchronise the Claude package and create a public release archive."""
import argparse
import json
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "research-writing"
COPY = ROOT / "plugins" / "research-writing" / "skills" / "research-writing"
FILES = ("README.md", "LICENSE", "CONTRIBUTING.md", "CHANGELOG.md", "VERSION", ".gitignore")
DIRECTORIES = ("skills", "plugins", ".claude-plugin", "examples", "scripts", "tests", ".github", "docs")


def tree(path):
    result = {}
    for item in sorted(path.rglob("*")):
        if item.is_symlink():
            raise ValueError("Package trees must contain regular files and directories.")
        if item.is_file() and "__pycache__" not in item.parts and item.suffix != ".pyc":
            result[item.relative_to(path).as_posix()] = item.read_bytes()
    return result


def manifests():
    version = (ROOT / "VERSION").read_text().strip()
    plugin = {"name": "research-writing", "version": version,
              "description": "Write readable research articles from drafts, proofs and data.",
              "author": {"name": "Snehal Raj"}, "license": "MIT"}
    market = {"name": "research-writing", "owner": {"name": "Snehal Raj"},
              "plugins": [{"name": "research-writing", "source": "./plugins/research-writing",
                           "description": plugin["description"], "version": version}]}
    return {ROOT / "plugins/research-writing/.claude-plugin/plugin.json": plugin,
            ROOT / ".claude-plugin/marketplace.json": market}


def sync():
    tree(SOURCE)
    if COPY.exists():
        shutil.rmtree(COPY)
    COPY.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, COPY)
    for path, value in manifests().items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2) + "\n")


def check():
    if not (SOURCE / "SKILL.md").is_file() or tree(SOURCE) != tree(COPY):
        raise ValueError("Generated Claude skill differs from the canonical skill. Run --sync.")
    for path, value in manifests().items():
        if not path.is_file() or json.loads(path.read_text()) != value:
            raise ValueError("Plugin metadata differs from VERSION. Run --sync.")


def public_files():
    paths = [ROOT / name for name in FILES]
    for name in DIRECTORIES:
        directory = ROOT / name
        tree(directory)
        paths.extend(p for p in directory.rglob("*") if p.is_file() and
                     "__pycache__" not in p.parts and p.suffix != ".pyc")
    for path in sorted(set(paths)):
        if not path.is_file() or path.is_symlink():
            raise ValueError("A required public file is missing or is a symlink.")
        yield path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sync", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--deny-token", action="append", default=[], help="Reject an archive containing this literal text")
    args = parser.parse_args()
    try:
        if args.sync:
            sync()
        check()
        paths = list(public_files())
        for path in paths:
            data = path.read_bytes()
            if any(token.encode() in data for token in args.deny_token):
                raise ValueError(f"A release exclusion token occurs in {path.relative_to(ROOT)}.")
        if args.archive:
            target = args.archive.resolve()
            if target.is_relative_to(ROOT):
                raise ValueError("Write release archives outside the source repository.")
            target.parent.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as bundle:
                for path in paths:
                    bundle.write(path, "research-writing/" + path.relative_to(ROOT).as_posix())
        print(f"Public package checks passed: {len(paths)} files.")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
