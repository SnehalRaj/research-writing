"""Install a complete skill without overwriting an existing local version."""
import argparse
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "research-writing"


def tree(path):
    result = {}
    for item in sorted(path.rglob("*")):
        if item.is_symlink():
            raise ValueError(f"Symlink in skill tree: {item.name}")
        if item.is_file():
            result[item.relative_to(path).as_posix()] = item.read_bytes()
    return result


def install(destination):
    target = destination / SOURCE.name
    if target.is_symlink():
        raise ValueError("The skill destination is a symlink; choose another destination.")
    if target.exists():
        if target.is_dir() and tree(target) == tree(SOURCE):
            print("This skill version is already installed.")
            return
        raise ValueError("The destination contains another version. Preserve or move it before installation.")
    tree(SOURCE)
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".research-writing-", dir=destination) as temp:
        staged = Path(temp) / SOURCE.name
        shutil.copytree(SOURCE, staged)
        if target.exists() or target.is_symlink():
            raise ValueError("The destination changed during installation.")
        staged.rename(target)
    print(f"Installed research-writing at {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--platform", choices=("codex", "claude"), required=True)
    parser.add_argument("--dest", type=Path, required=True, help="Parent directory for the installed skill")
    args = parser.parse_args()
    try:
        install(args.dest.expanduser())
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
