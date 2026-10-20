import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DistributionTests(unittest.TestCase):
    def test_platform_packages_match(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/package.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_install_handles_spaces_and_is_idempotent(self):
        for platform in ("codex", "claude"):
            with self.subTest(platform=platform), tempfile.TemporaryDirectory(prefix="skill test ") as temp:
                dest = Path(temp) / "my skills"
                command = [sys.executable, str(ROOT / "scripts/install.py"), "--platform", platform, "--dest", str(dest)]
                for _ in range(2):
                    result = subprocess.run(command, capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertTrue((dest / "research-writing/SKILL.md").is_file())
                self.assertTrue((dest / "research-writing/references/review.md").is_file())

    def test_install_preserves_conflicting_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp)
            target = dest / "research-writing"
            target.mkdir()
            (target / "SKILL.md").write_text("existing author skill")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"), "--platform", "codex", "--dest", str(dest)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual((target / "SKILL.md").read_text(), "existing author skill")
            self.assertEqual(list(target.iterdir()), [target / "SKILL.md"])

    def test_install_rejects_symlink_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            external = base / "external"
            external.mkdir()
            (base / "research-writing").symlink_to(external, target_is_directory=True)
            result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"), "--platform", "claude", "--dest", str(base)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(list(external.iterdir()), [])

    def test_release_archive_contains_only_public_files(self):
        import zipfile
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / "release.zip"
            result = subprocess.run([sys.executable, str(ROOT / "scripts/package.py"), "--archive", str(archive)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            with zipfile.ZipFile(archive) as bundle:
                names = bundle.namelist()
                self.assertIn("research-writing/skills/research-writing/SKILL.md", names)
                self.assertTrue(all("private" not in Path(name).parts and ".git" not in Path(name).parts for name in names))
                self.assertEqual(len(names), len(set(names)))

    def test_data_example_reproduces_summary(self):
        import json
        result = subprocess.run([sys.executable, str(ROOT / "examples/paired-results/summarise.py")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = json.loads(result.stdout)
        self.assertEqual(summary["seeds"], 5)
        self.assertAlmostEqual(summary["baseline_mean_accuracy"], 0.72)
        self.assertAlmostEqual(summary["candidate_mean_accuracy"], 0.73)
        self.assertAlmostEqual(summary["mean_difference_percentage_points"], 1.0)
        self.assertEqual(summary["seeds_improved"], 4)
        self.assertEqual(summary["seeds_worsened"], 1)

    def test_local_document_links_resolve(self):
        import re
        for directory in ("skills", "plugins", "examples", "docs"):
            for path in (ROOT / directory).rglob("*.md"):
                for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
                    if ":" not in target and not target.startswith("#"):
                        self.assertTrue((path.parent / target.split("#")[0]).exists(), f"{path}: {target}")
        for path in (ROOT / "README.md", ROOT / "CONTRIBUTING.md"):
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
                if ":" not in target and not target.startswith("#"):
                    self.assertTrue((path.parent / target.split("#")[0]).exists(), f"{path}: {target}")


if __name__ == "__main__":
    unittest.main()
