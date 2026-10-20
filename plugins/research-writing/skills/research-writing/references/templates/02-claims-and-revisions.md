# Templates: claims, proofs and revisions

Reusable working template. Select the fields required by the task. Keep original source material in the authorised working record.

## Claim record

```yaml
claim_id:
text:
kind: definition | theorem | numerical | hardware | literature | interpretation | proposal
objects_and_spaces:
conventions:
assumptions:
quantifiers:
conclusion:
source:
  version:
  locator:
  primary_link:
implementation_or_data:
checks_performed:
counterexamples_or_failures:
unresolved_questions:
source_fidelity: checked | partial | unchecked
validity: checked-with-scope | disputed | unchecked
summary_locations: []
author_decision:
```

## Proof review

| Step | Inference | Assumption or cited result | Independent check | Status |
|---|---|---|---|---|
| 1 |  |  |  |  |

Separate a checked identity from a numerical example.
Keep failed cases and the exact change that resolves or narrows them.

## Feedback and revision ledger

| ID | Exact feedback | Source and date type | Affected revision | Reader problem | Before | After | Preserved scope | Decision |
|---|---|---|---|---|---|---|---|---|
|  |  | message / meeting / archive commit |  |  |  |  |  |  |

Use separate entries when one comment contains several requests.
Record a deletion explicitly. Record the destination of moved technical details.
Keep the author's proposed factual wording separate from the checked wording finally accepted.

## Acceptance record

```yaml
unit:
source_revision:
review_pdf_identity:
changed_printed_pages:
changed_pdf_pages:
scientific_status:
editorial_status:
render_status:
author_exact_response:
accepted_scope:
remaining_open_items:
next_action:
```

Fill the author-response field from the author's explicit decision.
A commit, a build or text colour supplies a different kind of evidence.

## Record use

Keep source fidelity and validity separate even when both use the same source passage.
A source can state a claim accurately while its proof leaves an assumption unresolved.
Finite checks retain the tested range, statistic, tolerance and failures.
Record source identity before substituting an experiment, figure or theorem.

Keep planning permission, draft permission and final acceptance as distinct author decisions.
Record the exact unit, revision and language version that the author accepted.
Refresh changed page locators after the final render.
Retain the current unit, open questions and next action when the review pauses.
