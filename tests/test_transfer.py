"""Check that the installed reference package retains its usable detail."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/research-writing"
REF = SKILL / "references"


class CompleteTransferTests(unittest.TestCase):
    def test_full_reference_units_are_present(self):
        expected = ["writing-standard.md", "method.md", "author-style.md", "transfer-catalog.json",
            "rules/01-research-argument.md", "rules/02-exposition-and-terminology.md",
            "rules/03-claims-proofs-evidence.md", "rules/04-editing-and-compression.md",
            "rules/05-figures-and-proof-presentation.md", "rules/06-author-control-and-revision.md",
            "rules/07-adapting-the-method-to-papers.md", "critics/README.md",
            "critics/01-argument-and-prose.md", "critics/02-scientific-claims.md",
            "critics/03-exposition-and-terminology.md", "critics/04-presentation.md",
            "critics/05-evaluation-pipeline.md", "templates/01-narrative-and-paragraphs.md",
            "templates/02-claims-and-revisions.md", "templates/03-contributions-and-definitions.md",
            "cases/01-revision-lessons.md", "cases/02-failures-and-boundaries.md",
            "cases/03-critic-tests.json"]
        self.assertEqual([name for name in expected if not (REF / name).is_file()], [])

    def test_full_author_style_policy_is_retained(self):
        text = (REF / "writing-standard.md").read_text()
        self.assertEqual(re.findall(r"^(\d+)\. ", text, re.M)[:12], [str(i) for i in range(1, 13)])
        for concept in ("noun cluster", "positive instructions", "punchlines", "articles"):
            self.assertIn(concept, text)

    def test_structured_templates_retain_critical_fields(self):
        text = (REF / "templates/02-claims-and-revisions.md").read_text()
        fields = set(re.findall(r"^\s*([a-z_]+):", text, re.M))
        self.assertTrue({"objects_and_spaces", "assumptions", "quantifiers", "primary_link",
            "counterexamples_or_failures", "author_exact_response", "accepted_scope"} <= fields)

    def test_critic_cases_have_context_and_preservation_rules(self):
        cases = json.loads((REF / "cases/03-critic-tests.json").read_text())
        self.assertEqual(len(cases), 16)
        self.assertEqual(len({case["id"] for case in cases}), 16)
        for case in cases:
            for field in ("context", "text", "expected_finding", "preserve", "rules"):
                self.assertTrue(case[field], (case["id"], field))

    def test_rule_catalog_preserves_all_rule_ids_and_checks(self):
        rules = json.loads((REF / "transfer-catalog.json").read_text())["rules"]
        expected = {f"{prefix}{n:02}" for prefix, count in [("N",6),("E",5),("C",6),("X",5),("L",3),("V",3),("P",4)] for n in range(1,count+1)}
        self.assertEqual({rule["id"] for rule in rules}, expected)
        for rule in rules:
            self.assertTrue((REF / rule["destination"]).is_file())
            self.assertTrue(rule["preservation_checks"])

    def test_all_canonical_resources_are_in_the_release_manifest(self):
        names = set((ROOT / "release-files.txt").read_text().splitlines())
        for path in SKILL.rglob("*"):
            if path.is_file() and "__pycache__" not in path.parts:
                relative = path.relative_to(SKILL).as_posix()
                self.assertIn("skills/research-writing/" + relative, names)
                self.assertIn("plugins/research-writing/skills/research-writing/" + relative, names)


if __name__ == "__main__":
    unittest.main()
