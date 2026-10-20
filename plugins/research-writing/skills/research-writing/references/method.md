# From research material to a reviewed document

Use this method for a paper, a contribution chapter or a full thesis.
Scale the records to the task. A local wording fix can use the small-edit route below.

For a substantial revision, complete the preparation stages before choosing the narrative.
Read the sources, extract all contribution candidates with their evidence and status, then inventory definitions and dependencies.
Narrative planning follows this inventory. Drafting and critic assignment follow the plan.
This order prevents an early story from hiding a contribution, an unresolved claim or a missing definition.

## 1. Read the material and define the task

Read the complete target before judging its structure or style.
Read the source material needed to understand each contribution and claim within scope.
Record the source revision, paper versions, datasets, figure assets and existing author decisions.
Record hashes or other stable identities for source files and result assets when a later comparison needs them.

State the audience, document type, length constraints and permitted changes.
Separate new research from an account of existing research.
Use the author's current instructions to set voice, protected wording and review boundaries.
A request for a complete revision authorises a complete review draft within that scope.
Keep acceptance of the final wording as a separate decision.

Treat AI-generated proofs and summaries as unverified material.
Preserve their sources and failed cases so later revisions remain traceable.
Use the [source and claim template](templates/02-claims-and-revisions.md).

**Output:** a source inventory, a recoverable baseline and the edit scope.
**Exit check:** every result has an identifiable source or an explicit unresolved status.
Keep any source that remains unread or unavailable visible in the record.

## 2. Extract the contributions and establish their evidence

Extract all contribution candidates before selecting a central argument.
Include constructions, formal results, empirical findings, negative results and useful interpretations that the sources present.
For each candidate, record its source locator, content, assumptions, evidence, status and dependencies.
Retain candidates that may be omitted. Record the reason when the later plan excludes them.
Use the [contribution inventory](templates/03-contributions-and-definitions.md).

Extract the claims, experiments and comparisons before polishing prose.
Separate the method as defined, the method implemented and the result measured.
Check definitions, proofs, numerical values and baseline descriptions against the actual sources.
A source can support an accurate transcription while leaving the mathematics disputed.
Record these outcomes separately.

For a theorem, fix the conventions and reconstruct the proof.
Inspect boundary cases that follow from the assumptions.
For an experiment, trace the prediction and metric through the implementation to the data.
Use small independent tests when they can expose a specific error.
Preserve the input, tolerance and any failed case.
Keep a claim unresolved when the evidence does not settle it.

A writing critic can identify missing evidence. Its finding alone gives no authority for new experiments or replacement results.
Record the study that would resolve a material issue.
Seek the author's direction when that study falls outside the authorised task.
Continue independent work within scope.

**Output:** a complete contribution inventory, claim records, proof checks and an evidence map.
**Exit check:** every candidate has an evidence status.
Critical claims have support or remain excluded from final assertion pending resolution.

## 3. Inventory definitions and dependencies

Inventory every concept, symbol and acronym needed to explain or check the contributions.
Record each object's definition, space, conventions, first use and later uses.
Include terms introduced by captions, figures, tables and summaries.
Use the [definition and dependency inventory](templates/03-contributions-and-definitions.md).

Map dependencies between definitions, methods, formal results, experiments and their explanations.
Distinguish a shared definition from a contribution-specific extension.
Find forward references, circular dependencies and objects that lack a definition.
Retain an unresolved entry when the source leaves a dependency unclear.

Record where existing definitions and supporting derivations currently sit.
A proposed cut needs a destination for every dependency that later text still uses.
Complete this inventory before the narrative plan, substantial rewriting or critic assignment.

**Output:** a definition inventory and a dependency map linked to the contribution inventory.
**Exit check:** each contribution's prerequisites have a source, a planned definition or an explicit unresolved status.

## 4. Elicit the author's argument

Use the inventories to ask which question the document can answer and why that question matters.
Ask the author to explain the problem, the research choice and what the evidence changed in their view.
Capture that reasoning before replacing it with formal prose.
Use an existing author account when it already answers these questions.
Ask a focused question when a missing reason blocks the argument.

Test whether the proposed account connects these elements:

> A meaningful problem → a specific difficulty in existing work → a reason for the research choice → evidence → a supported conclusion.

Use this chain to test reasoning. Adapt its order and form to the contribution.
A counterexample or negative result needs an account of what failed and what follows from that failure.

Write the [narrative brief](templates/01-narrative-and-paragraphs.md).
Check it against every contribution candidate before choosing the central claim.
Explain each exclusion and preserve the candidate's evidence status.

**Output:** a narrative brief linked to the contribution inventory.
**Exit check:** the proposed argument reflects the author's research choice and the evidence's limits.
Record author recognition or acceptance when the task requires it.

## 5. Assign jobs to sections and paragraphs

Give each section a reader question.
Give each paragraph a distinct job within that section.
Set a length target that fits the job and the audience.
Choose headings around the central subject.
Preserve protected headings when the task limits structural changes.

Assign every major result, figure, table and proof to a destination.
Use the dependency inventory before moving or deleting definitions.
For each paragraph, record its connection to the previous paragraph and the evidence it uses.
Keep useful detail where readers need it.

Use the [exposition rules](rules/02-exposition-and-terminology.md) and [compression rules](rules/04-editing-and-compression.md).
For a paper, also use the [paper adaptation](rules/07-adapting-the-method-to-papers.md).

**Output:** a paragraph map, a figure plan, length targets and destinations for retained dependencies.
**Exit check:** every essential contribution has a destination or an explained exclusion.
Paragraphs with the same job need a distinct reading purpose.

## 6. Draft within the authorised scope

Write from the source evidence, inventories and the author's account.
Lead with a concept or result at the reader's level.
Place the mechanism, definitions and qualifications where readers can understand them.
Keep a scientific correction's explanation in the passage that readers will see.
Store its review history in working records.

Preserve accepted wording outside the edit scope.
Mark new text for review and retain a before-and-after record.
Use the authorised review unit, such as a subsection or a coherent claim group.
An authorised batch can proceed to combined review when its scope is explicit.

Change a result asset or mathematical construction only within the task's scientific authority.
A prose repair alone does not authorise either change.
Keep unresolved scientific claims visibly pending in the working record.
Give the manuscript the supported scope or explicit source attribution where required.

**Output:** a review draft and a change ledger.
**Exit check:** the draft follows the planned argument and changes only authorised material.
All removed details have an explained omission or a destination.

## 7. Review science, argument and presentation separately

Assign bounded reviews after the preparation and narrative records exist.
Use the [critic briefs](critics/README.md).
Give critics the current revision, inventories, relevant sources and protected author decisions.

The scientific critic checks validity and source fidelity.
The argument critic checks purpose and the reasons between sentences.
The exposition critic checks definitions, terminology and level of detail.
The presentation critic checks figures, citations and rendered pages.

Require exact quotations or locators, a reason and evidence for each finding.
Record severity and uncertainty.
Include missing contributions and excessive compression in the review.
Let a reviewer recommend keeping a phrase when it carries a necessary condition.
A style flag prompts a contextual reading.

Reconcile conflicting findings before applying repairs.
The author resolves taste and scope choices.
Sources, calculations and valid arguments resolve scientific questions within their limits.

**Output:** individual findings with evidence, severity, uncertainty and proposed dispositions.
**Exit check:** each conflict has a resolution or an explicit open status.
The editor has identified the smallest adequate repairs.

## 8. Revise and verify the affected dependencies

Resolve scientific blockers before polishing their explanations.
Then improve flow and remove repeated or empty prose.
Check summaries, captions and conclusions after narrowing a claim.
Check references after moving definitions or proofs.
Update the inventories when a scientific correction changes an object or dependency.

Build the exact review revision when the output format requires it.
Inspect changed pages and the neighbouring pages needed to assess the layout.
Inspect the full output after a complete rewrite.
Check values, retained figures and protected passages against the baseline.
Check translations for the same argument and claim scope.
Use the [render checks](rules/05-figures-and-proof-presentation.md#minimum-render-check).

**Output:** a revised draft, a verified diff, the exact build identity and a reviewed page list.
**Exit check:** required evidence and render checks cover the exact revision delivered.
Record any check that remains open or that an older revision has made stale.

## 9. Obtain acceptance and record its scope

Give the author a concise before-and-after account, unresolved decisions and exact pages to inspect.
Use a comparison table when it makes a substantial revision easier to review.
Record acceptance, rejection or requested changes against the source revision and target passage.
If the author rejects the direction, restore the chosen baseline before another attempt.

An accepted section can later change.
Reopen review for the affected text and dependencies when new evidence or an instruction warrants it.
Stop polishing accepted prose when no new defect or instruction justifies a change.

**Output:** an acceptance record and a recoverable checkpoint.
**Exit check:** the author has accepted the wording when acceptance is required.
Keep source fidelity, scientific verification, editorial quality, rendered layout and author acceptance as separate states.
Draft delivery can finish an authorised revision task while final wording remains pending author acceptance.

## Small-edit route

For a local change, record the request and inspect its context.
Apply the change, check the diff and render when layout can change.
Use the broader process when the change affects a claim, a definition or the document's argument.
A corrected word rarely needs a fresh contribution inventory.
