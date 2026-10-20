# Match each claim to its evidence

These rules define a verification method.
Use their records to show what each check established and what remains unresolved.
Applying the rules alone gives no certificate for every theorem in a document.
The examples below are synthetic teaching examples.

## C01. Label the kind of claim

Classify each claim as a definition, proved result, numerical observation, hardware measurement, literature result, interpretation or proposal.
Record its source and the scope of its support.
Choose a verb that matches that class: define, prove, observe, measure, infer or propose.

A successful finite experiment supports its measured result.
An asymptotic statement needs an argument with the relevant assumptions.
Recheck an accepted sentence when the underlying model changes.
Author acceptance records a wording decision; keep its scientific evidence status explicit.

**Synthetic example:** A model reuses feature parameters across graph sizes.
That design property alone leaves the full model's trainability unresolved.
A claim of proved trainability needs a theorem for the actual architecture and its assumptions.
Keep the supported design claim and the open trainability claim separate in the evidence record.

**Check:** Does the claim's verb match both its evidence type and its supported scope?

## C02. Carry assumptions into the actual claim

Write a claim record before polishing a theorem:

1. Identify the objects, spaces and conventions.
2. List the assumptions and quantifiers.
3. State the conclusion and what varies in it.
4. Trace each proof step to an assumption or an established result.

Check surrounding summaries, captions and conclusions against that record.
A narrow theorem supports only the scope established by its hypotheses and conclusion.
Put conditions where the claim needs them.
A generic caution at the end can leave the actual missing assumption hidden.

**Synthetic example:** A graph construction applies edge operations in sequence.
A permutation claim may need a rule for transporting that order under node relabelling.
A later encoding claim may also require uniform node amplitudes.
Check each requirement against the actual construction and theorem.
The requirements concern separate objects and need separate evidence.

**Check:** Can a reader recover the essential input scope from the result and its immediate explanation?

## C03. Verify the source and its use

Confirm that the cited paper exists, its metadata matches and its link reaches the intended version.
Inspect the result being cited, including assumptions and notation.
Record the theorem, equation, figure or page that supports the manuscript's claim.

A source transcription can preserve an error or ambiguity.
Keep source fidelity and mathematical correctness as separate checks.
Paraphrase explanatory language.
Preserve exact definitions when their wording matters and attribution permits their use.

Inspect rendered bibliography entries as well as source records.
A successful build can leave wrong metadata, an incorrect version or an unusable link.
Check the destination that the reader can actually open.

Present the author's contribution directly in the manuscript's chosen voice.
Follow the author's publication and attribution rules for self-citations.
Use a self-citation when it directs readers to useful omitted material.
Keep exact source provenance in working records.
Preserve necessary scientific citations and qualifications in the manuscript.

**Check:** Does the cited result support this use under the manuscript's own assumptions?

## C04. Verify the object that the experiment computes

Trace the path from input through model, training objective, prediction and evaluation metric.
Record simulation, sampled noise and hardware execution separately.
Check what each baseline changes and what the comparison holds fixed.
Preserve the identity of the reported experiment when correcting its description.

**Synthetic example:** A classifier combines several amplitude vectors to form a prediction.
Describe that prediction rule before interpreting its score.
If a shot estimate covers only a component gradient protocol, state that scope beside the estimate.
Record an uncounted amplitude readout cost when it changes the result's interpretation.
A repaired model description can preserve the original measured scores.

For a representation-editing method, identify the hidden representation and the intervention applied to it.
An intervention on a representation differs from a change to the model's weights.
Trace the implementation before choosing that description.

Check leading-performance claims against the actual table, task and comparator set.
Keep seeds, uncertainty and selection procedures in the reproducibility record.
Results prose can stay concise while these details remain accessible.

**Check:** Does the prose describe the prediction and metric that the implementation actually computes?

## C05. Check proofs with independent evidence

Have a reviewer reconstruct the argument from the statement and definitions.
Ask for missing assumptions, boundary cases and counterexamples before a polished proof.
For computational checks, build a small independent instance and retain failed cases.
Record the convention, input and tolerance with the outcome.

Useful checks include dimensions, normalisation, zero inputs, sign conventions and composition order.
Choose checks from the claim's assumptions and possible failure cases.
Cases that an implementation already handles easily can leave the disputed condition untested.

Numerical agreement can detect mistakes within the tested cases.
A universal result still needs a valid proof.
Agreement between language models provides no proof certificate.

When a result fails, record the failure and the smallest scientifically valid repair.
The author decides whether to narrow the claim, change the construction or remove the result.
Keep a proposed repair in the review record until its scientific authority is clear.
An audit finding alone gives no authority to replace the research contribution.

**Check:** Can another reviewer reproduce the failed case and see which claim or assumption it tests?

## C06. Give citations the work they can perform

A citation can establish an existing construction under its own assumptions.
Check the mapping from those assumptions to the manuscript's case.
A relevant topic or a nearby reference can leave a required proof step unresolved.

**Synthetic example:** A proof needs equivariance under node relabelling.
A cited graph-canonicalisation procedure helps only if the proof establishes the required mapping and conditions.
Appending references after the proof leaves that obligation in place.

For hardness and advantage claims, distinguish the computational task, access model, ensemble and useful learning objective.
Retain these distinctions in the claim record.
Keep the qualifications required by the published result.
A large state space or sampling-hardness result alone leaves a learning-advantage claim unsupported.

**Check:** Identify the exact inference supplied by each citation and any remaining obligation in the manuscript.
