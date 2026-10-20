# Critic: scientific claims and proofs

Reusable guide. This guide transfers an earlier writing method. Its review judgements have no independent accuracy benchmark.

## Task

Review the scientific account against the actual sources, assumptions and implementation.
Record whether each important claim is checked, partly checked or unchecked.
Keep source fidelity and correctness as separate judgements.

## Tests

1. Classify the claim's evidence type and quantifiers.
2. Reconstruct the mathematical objects and conventions.
3. Compare the claim with the cited result and its assumptions.
4. Trace experiments to the predictor, loss, readout and metric actually used.
5. Check summary and caption claims for scope expansion.
6. Search for missing cases, counterexamples and omitted source contributions.

For a proof, list each inference and the result that justifies it.
Test boundary cases chosen from the assumptions.
Separate an algebraic identity from an empirical check or a heuristic argument.

For an experiment, check figure identity, comparator settings and the reported statistic.
A different dataset or implementation requires an explicit record and author approval.
Do not silently replace source results with a nearby run that appears more convenient.

## Source-derived tests to adapt

- Does equivariance include all input metadata and the gate schedule used in the construction?
- Does the state preparation match the theorem's uniformity and normalisation assumptions?
- Is the reported model a vector ensemble, a density mixture or another predictor?
- Do the resource estimates cover only component gradients, or also the readout needed by the full predictor?
- Does the baseline modify weights or hidden representations?
- Does parameter reuse apply to the full model or only to a component?

These questions come from earlier technical reviews.
Adapt each question to the current model and check whether its premise applies.

## Verdict

Report a blocker only with a concrete conflict, unsupported essential step or missing evidence necessary for the claim.
Offer repair options: narrow the statement, add an assumption, repair the proof or leave it unresolved.
Do not claim universal correctness from passing finite tests or agreement among reviewers.

## Evidence boundaries

Check the input metadata, edge order and chronological schedule when testing an equivariance claim.
Distinguish canonical labels, transported orders and choices fixed under automorphisms.
Each construction needs its own argument.

Check zero input rows and later preparation reuse when normalisation changes the theorem's input.
Keep component transfer, observed gradients and full-model trainability as separate claims.
Carry a narrowed result into the abstract, early summary, conclusion and captions.
A nearby caveat cannot change another sentence's quantifiers.

Separate predictive accuracy from hardware agreement within a stated tolerance.
Use a common resource definition when comparing evaluations, measurement shots or elapsed time.
Preserve differences in bias, variance and sampling rules under shared estimator notation.
Verify the cited work's identity and the exact result that supports the claim.
A working link alone leaves theorem support unchecked.

## Check omissions and underclaims

Compare the revision with the contribution inventory for lost results, hypotheses and evidence.
Report a dropped hypothesis even when the revised theorem sounds plausible.
Report an underclaim when the source supports a stronger contribution that the revision hides.
State that contribution with its exact task, comparator, metric and resource scope.
Scientific qualifiers can determine meaning. Preserve them when removing vague or rhetorical language.
A missing source creates an evidence gap; record the gap before proposing a new factual statement.
