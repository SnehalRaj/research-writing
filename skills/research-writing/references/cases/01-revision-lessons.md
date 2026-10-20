# Revision lessons

Every passage below is an original synthetic adaptation. These passages contain no private manuscript quotation.
The conditions form part of each lesson. They prevent a useful edit from changing its scientific meaning.

<a id="e01"></a>

## E01. Give historical material a research purpose

**Status:** original synthetic adaptation.

**Context:** An opening surveys earlier model families. The author chose the history to explain scale and the role of experiments.

**Before**

> Early predictors used small datasets. Later models used larger datasets and faster processors. Several model families fell out of use and later returned.

**After**

> We revisit these model families to ask how a useful small model can remain useful as data and computation grow. Their changing performance also explains why experiments guide our design choices.

**Reason:** The revision states the question that makes the historical facts useful. The facts can then support the research position.

**Preserve:** The reason for revisiting the history. The role of empirical evidence in the author's research choice.

**Conditions:** The surrounding sources must support any historical statement that remains. This is an opening about scale; another research question can need another history.

**Rules:** N01, N02, N03.

<a id="e02"></a>

## E02. Name a concrete future study

**Status:** original synthetic adaptation.

**Context:** A proposed sensor model has a construction and a cost analysis. The study has no learning-task experiment.

**Before**

> Its practical value requires further assessment.

**After**

> We leave tests of the sensor model on noisy classification tasks for future work.

**Reason:** The revision names the unresolved action and model. It belongs beside that proposal or in the discussion.

**Preserve:** The absence of task-level evidence. The proposed status of the study.

**Conditions:** Use this sentence only when the named study remains open. A section that already reports the test must state the completed action.

**Rules:** X02.

<a id="e03"></a>

## E03. State the metric's precise invariance

**Status:** original synthetic adaptation.

**Context:** A synthetic experiment compares coefficient magnitudes. Its score uses only those magnitudes.

**Before**

> This score cannot establish complete agreement between the states.

**After**

> Changing coefficient signs leaves the magnitude score unchanged.

**Reason:** The revision states exactly which information the score discards. The experimental limitation remains in the printed account.

**Preserve:** The distinction between magnitude agreement and sign agreement.

**Conditions:** The score must use magnitudes alone. A phase-sensitive metric needs its own analysis.

**Rules:** X05, C04.

<a id="e04"></a>

## E04. Describe the computation behind a curve

**Status:** original synthetic adaptation.

**Context:** Each point reuses a different subset of one fixed set of device outputs. No new device batch runs between points.

**Before**

> The curve shows how the input fraction changes the prediction. Each fraction does not correspond to a new device experiment.

**After**

> The curve shows how subsets of the cached device outputs affect the prediction.

**Reason:** The operational account identifies the data source and varied choice. It removes the need for rhetorical correction.

**Preserve:** The cached origin of the device outputs. The predictor and the experimental values.

**Conditions:** The outputs really must come from a fixed stored batch. A curve from fresh runs requires different wording and uncertainty.

**Rules:** L02, C04.

<a id="e05"></a>

## E05. Keep a failure mode while removing a generic demand

**Status:** original synthetic adaptation.

**Context:** A reconstruction score detects faults. Some faulty samples also have low reconstruction error. The paragraph introduces no new validation procedure.

**Before**

> Faulty samples can reconstruct accurately, so the score needs careful validation.

**After**

> Faulty samples can also have low reconstruction error.

**Reason:** The concrete failure explains the interpretation limit. The generic validation instruction adds no local result or action.

**Preserve:** The false-negative mechanism.

**Conditions:** Retain any threshold or validation procedure that the argument actually uses. The cut applies to an empty instruction, after checking the surrounding section.

**Rules:** X01, X05.

<a id="e06"></a>

## E06. Keep a protocol-specific measurement cost

**Status:** original synthetic adaptation.

**Context:** The paragraph concerns the standard local Pauli classical-shadow estimator. Accuracy and confidence are fixed. The requested observable has Pauli weight w.

**Before**

> Measurement cost depends on the observable, error and confidence. Local Pauli shadows can need exponentially many shots for high-weight Pauli observables.

**After**

> For local Pauli shadows, the required shot count can grow exponentially with the Pauli weight.

**Reason:** The revision removes a generic list while retaining the cost limitation and the measurement protocol that causes it.

**Preserve:** The local Pauli shadow protocol. The weight-dependent limitation.

**Conditions:** Keep the stated accuracy and confidence accessible in the method record. Direct measurement of one chosen Pauli string does not inherit this weight dependence from the shadow protocol.

**Rules:** X01, X05.

<a id="e07"></a>

## E07. Name the object of an exact identity

**Status:** original synthetic adaptation.

**Context:** The section defines the expectation h(alpha). The identity applies to that function under the listed generator assumptions.

**Before**

> The equality holds for the stated expectation.

**After**

> The equality holds for the expectation h(alpha) defined in the preceding paragraph.

**Reason:** The revision supplies a checkable antecedent. It keeps the identity tied to the same function.

**Preserve:** The actual expectation and its assumptions.

**Conditions:** Check that h(alpha) exists at the stated location. Supply the definition if a section move removed it.

**Rules:** E02.

<a id="e08"></a>

## E08. Give a definition its domain and reference measure

**Status:** original synthetic adaptation.

**Context:** The section uses an ensemble of unitaries on C^r. A moment comparison requires the dimension and the Haar group.

**Before**

> A unitary 2-design has the correct moments in this representation.

**After**

> For unitaries on C^r, a unitary 2-design matches the Haar averages over U(r) of U^{tensor t} tensor conjugate(U)^{tensor t}, for t = 1, 2.

**Reason:** The revision identifies the space, group and moment operation. A vague adjective replacement would leave the definition incomplete.

**Preserve:** The Hilbert-space dimension. The first two unitary moments and their Haar reference.

**Conditions:** Use the manuscript's tensor and complex-conjugation conventions. Check that the claimed representation matches the result that follows.

**Rules:** E02, E05, C02.
