# Contributions and definition dependencies

Complete this preparation packet before a narrative, prose rewrite or expert critic assignment.
For a local edit, update only the affected entries and their dependencies.
Keep the packet in working notes. Manuscript readers need the research account and its scientific limits.

## Source boundary

```yaml
preparation:
  task: ""
  audience: ""
  output_form: ""
  authorised_stage: ""
  sources: []  # identity, version or hash, complete unit read, locator
  excluded_sources: []  # author boundary or reason unavailable
  existing_drafts: []  # identity, purpose, author acceptance status
  unresolved_evidence: []
```

Read the complete agreed source set. Record source-reported findings separately from independently checked findings.
Mark missing raw data as an evidence limit. It cannot silently erase a reported result or verify that result.

## Contribution inventory

Create one entry per distinct candidate. A paper may contain a useful method even when its usefulness study remains planned.
Keep developed proposals in the inventory with their actual status.

```yaml
contributions:
  - id: C01
    short_name: ""
    source_locator: ""
    source_version: ""
    source_ownership: "prior work, present authors, collaborator, or unresolved"
    scientific_type: "definition, construction, theorem, observation, interpretation, tool, or study proposal"
    work_status: "specified, implemented, proved, measured, proposed, or unresolved"
    result_or_deliverable: ""
    research_question: ""
    relation_to_prior_work: ""
    novelty_evidence: "checked sources and limits of the search"
    objects_and_spaces: []
    assumptions: []
    quantifiers: []
    comparator: ""
    metric_and_units: ""
    tested_population_and_range: ""
    data_and_code_available: ""
    evidence_status: "source-reported, reproduced, independently verified, or unavailable"
    evidence_locator: ""
    uncertainty_and_failures: []
    supported_scope: ""
    unsupported_extensions: []
    depends_on: []  # contribution or definition IDs
    author_interpretation: ""
    current_location: ""
    candidate_destination: "undecided until the inventory is complete"
    open_question: ""
```

Check the abstract, methods, results, discussion, captions and supplement for candidates.
Include calibration choices and reusable artifacts when the work develops them.
Keep a proposed evaluation distinct from a completed demonstration of usefulness.
Treat “first”, “general”, “faster” and “validated” as claims that need their own evidence.
Separate theorem validity from source fidelity. Record counterexamples and the tested tolerances.

## Definition inventory

```yaml
definitions:
  - id: D01
    term_or_symbol: ""
    object_type_and_domain: ""
    reader_question: "why the reader needs this object"
    informal_meaning: ""
    formal_definition: ""
    source_locator: ""
    current_first_use: ""
    current_definition_location: ""
    prerequisites: []  # definition IDs
    assumptions_or_conventions: []
    scope: "shared or local"
    contributions_that_use_it: []
    proposed_first_definition: ""
    definition_form: "inline emphasis, equation with explanation, or formal statement"
    ambiguity_or_missing_detail: ""
```

Define an acronym when the full term first matters. Give a new technical term its own clause or sentence.
Explain a construction's purpose before its components and its operation before its performance claim.
Define evaluation criteria before score comparisons. Identify the population before its denominator or rate.
Preserve distinctions such as a classical probability and a quantum state, or evaluation counts and elapsed time.

## Dependency map and preparation check

Write each dependency as `prerequisite -> object or claim that uses it`.
Give a short reason for the arrow. Split overloaded terms and check cycles.
Choose a reading order that satisfies the dependencies with little repeated background.
State which definitions the audience can reasonably know and which this article must supply.

Before proceeding, check:

- Every contribution candidate has an owner, source, work status and evidence status.
- Every number has a population, metric, unit and source where applicable.
- Every technical claim has its necessary definitions, assumptions and quantifiers.
- Missing evidence and planned work remain visible in the packet.
- The author profile records current instructions and the status of its example passages.

If a necessary source is missing, record the gap and continue independent preparation.
Proceed to the narrative and [paragraph map](01-narrative-and-paragraphs.md) within the user's authorised scope.
Keep later author acceptance tied to the exact unit, version and scope reviewed.
