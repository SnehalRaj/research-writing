# Critic briefs and evaluation

Reusable guide. This guide transfers an earlier writing method. Its review judgements have no independent accuracy benchmark.

These briefs are proposed reusable review tools.
Their transfer does not install agents or establish performance on an independent document set.
Use them on a section with enough surrounding text to judge its argument.

The four roles cover argument, science, exposition and presentation.
They also check lost contributions, author scope and excessive compression.
Keep supplied reviewer evidence separate from inferred or simulated style preferences.

## Common inputs

Provide the target revision, the author brief, the paragraph map and protected decisions.
Provide the claim records and relevant source passages.
Include the rendered pages for a presentation review.
Mark unavailable evidence clearly.

## Roles

| Critic | Question | Output |
|---|---|---|
| [Argument and prose](01-argument-and-prose.md) | Does the reader understand the point and the reasons connecting it? | Located gaps, redundant jobs and useful passages to preserve |
| [Scientific claims](02-scientific-claims.md) | Does the statement follow from its evidence under the actual assumptions? | Supported, disputed and unchecked claims; minimal repair options |
| [Exposition and terminology](03-exposition-and-terminology.md) | Can the intended reader follow the objects and mechanism? | Definition, notation, sequencing and detail-placement issues |
| [Presentation](04-presentation.md) | Do figures, captions, references and layout support the argument? | Page-specific defects and checks |

Separate reviewers can run these roles independently when the user authorises that workflow.
A single editor can also run the checks in sequence for a small task.
No critic may change the manuscript without the authorised editing step.

## Required finding format

```yaml
id: finding-001
revision: source-commit
location: path, line or stable paragraph ID
quote: exact text
category: science | argument | exposition | presentation | scope
severity: blocker | important | optional
diagnosis: the concrete reader or scientific problem
evidence: source locator and relevant assumption, or null
evidence_status: checked | partial | unavailable
author_decision: relevant instruction or null
recommendation: keep | cut | move | clarify | verify | ask-author
minimal_repair: required content or action
preserve: claim, evidence or wording that must survive
uncertainty: what this reviewer could not establish
```

## Editor's decision rules

Resolve evidence conflicts before style conflicts.
Separate the author's scientific intent from a proposed formulation that may overstate it.
Follow explicit author choices on taste and structure when they preserve accuracy.
Record disagreement with a critic and its reason.

Do not combine scores into a single pass mark that hides a scientific blocker.
Do not require a fixed number of findings.
Use the [evaluation procedure](05-evaluation-pipeline.md) and [test cases](../cases/03-critic-tests.md) to check critic behaviour.

## Evidence and authority gates

Complete the contribution inventory and definition inventory before assigning a manuscript review.
Record each required input as available, partial or unavailable.
If a missing input blocks a necessary conclusion, report the gap and keep that conclusion open.
The briefs remain resources until the user authorises a review.

The current author brief and governing project rules control scope, voice and acceptance.
Apply an earlier preference only where it fits the current task.
Use the six verdicts in the evaluation guide; retain their separate evidence records.
A source hash establishes identity. A finite numerical check establishes only its tested cases.
A build establishes compilation. Each result needs the corresponding semantic or visual check.

## Protected content

Carry protected passages, result assets, conditions, counterexamples and approved structural choices into every brief.
Each critic must report useful content that a proposed edit would lose.
Record the destination of moved detail. Retain a recoverable source revision.
The editor resolves the evidence and author decisions before an authorised edit.

## Quotes, uncertainty and scores

Retain exact source quotations when the task needs them. Apply house style to the surrounding explanation.
Mark a quoted historical error or obsolete preference with its context and status.
A critic must identify missing source evidence before proposing a factual repair.
Keep the claim unchecked when the missing evidence prevents a decision.

Style-tool scores and model-generated scores supply diagnostic candidates.
They cannot establish scientific correctness, writing quality or author acceptance.
Keep the evidence and a human-readable diagnosis beside every material finding.
