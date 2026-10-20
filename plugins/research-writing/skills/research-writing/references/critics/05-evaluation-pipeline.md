# Evaluate a revision and the critics that review it

Reusable guide. This guide transfers an earlier writing method. Its review judgements have no independent accuracy benchmark.

This is a proposed evaluation procedure. Earlier local checks covered resource structure.
The critic judgements and expected case labels need author review.
No independent benchmark of reviewer accuracy has been run.

## Keep six verdicts

| Dimension | Question | Evidence |
|---|---|---|
| Source fidelity | Did the revision preserve the intended research material? | Source map, retained results and figure identities |
| Scientific validity | Do the claims follow under their actual assumptions? | Derivations, source results, counterexamples and scoped tests |
| Argument | Can readers follow why each claim and method appears? | Narrative brief and paragraph review |
| Exposition | Can the intended reader understand the objects and mechanism? | Definition order, notation and dependency checks |
| Presentation | Does the rendered document support that reading? | Page inspection, reference and figure checks |
| Author control | Does the revision match the request and acceptance state? | Scope, diff and explicit decision |

Give each dimension one of four states: **pass**, **revise**, **unchecked**, or **not applicable**.
Explain each revise or unchecked state with a locator.
A scientific blocker prevents final acceptance even if every stylistic dimension passes.
An unchecked critical result stays visibly open.

## Cheap checks before semantic review

Run checks for missing citations, unresolved labels, duplicate definitions and changed numerical values.
Compare approved source hashes and figure inputs.
Find repeated paragraphs, vague antecedents and stock phrases for manual inspection.

These checks produce candidates. They should not automatically delete sentences or replace terms.
Use the claim map to identify where a flagged sentence contains a necessary assumption.

## Semantic review

Review bounded sections with their context and evidence.
Ask each critic for findings in the [common format](README.md).
Merge duplicate findings without losing source locators.
Resolve factual disagreements against the source or calculation.
Resolve taste questions through the author brief and explicit decisions.

Record the action as accept, narrow, reject, defer or ask the author.
Explain rejected critic advice when it conflicts with the evidence or a deliberate structural choice.
Recheck only the changed section and affected dependencies unless a new issue warrants a wider audit.

## Test critic behaviour

Use the [contrast cases](../cases/03-critic-tests.md) before applying a new critic prompt to a manuscript.
Each case includes the text, context, expected finding and a required preservation rule.
Test generic prose and scientifically necessary qualifications separately.

The expected answers in this collection are editorial specifications.
They require author confirmation before becoming a benchmark of personal style.
Keep a separate set of unseen examples when comparing prompt versions.

For a labelled set, record:

- Critical misses and false scientific alarms.
- Useful edits proposed and accepted passages needlessly disturbed.

When enough labelled cases exist, calculate precision and recall by category.
Report sample size and ambiguous cases. Do not infer performance from this collection's word count or source coverage.

## Test repair quality

Give the editor the original passage, the finding and the protected content.
Compare the repaired passage with the original evidence and paragraph job.
Check whether the repair introduces a new claim, removes a condition or adds another generic closing sentence.

A shorter passage is an improvement only if it preserves the necessary explanation and evidence.
A longer passage can improve the document when it supplies the missing mechanism.
Record the reason for either choice.

## Stop rule

Stop when the required checks pass, the author accepts the revision and no unresolved critical finding affects it.
Avoid polishing accepted text to satisfy a score.
New evidence or an author request can reopen the relevant review unit.

## Review and acceptance record

Use the [acceptance record](../templates/02-claims-and-revisions.md#acceptance-record) for the reviewed unit and exact revision.
Record the inspected file identity and both printed and PDF page locators.
Keep these coverage states distinct: unreviewed, skimmed, discussed, revised pending acceptance, and accepted.
A change to accepted wording reopens the changed scope.

Respect an authorised phase sequence. Approval of a review process does not accept later wording.
Accept only the section, appendix or language version named in the author's decision.
A translation needs checks of the argument, paragraph jobs and scientific scope.
Record its own acceptance.

A declined critic recommendation stays in the ledger with the author's reason.
Restore the recoverable baseline when the author rejects a rewrite.
Preserve unrelated approved changes and document the exact restoration scope.
Expected labels for synthetic cases specify intended editorial behaviour.
They provide no measured performance result until a labelled evaluation has run.
