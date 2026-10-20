# Explain concepts and control terminology

Use the definition and dependency inventory before moving or shortening an explanation.
Keep precise scientific terms when a simpler substitute would change their meaning.
The examples below are synthetic teaching examples.

## E01. Give the construction before its parts

Name what the model does and why it needs its parts.
Then introduce registers, parameters and operations in the order readers will use them.
Open a methods section with reasons as well as instructions.
Connect the construction to the limitation or capability established in the preceding section.

**Synthetic example:** A feature loader uses a node register to control which feature state it prepares.
Give that idea before its state equation, normalisation and higher-order extension.
An opening full of register weights and indices can hide the mechanism that gives those objects a purpose.

**Check:** Can a reader state the construction's purpose before encountering its detailed notation?

## E02. Define each object before using it

Check the object's name, symbol, space and role.
Expand an acronym at the reader's first encounter, including an abstract or chapter summary.
Mark an inline definition when that convention helps recognition.
Use a formal definition environment for precise concepts that later results reuse.

Name an actual representation when a vague reference would leave the object unclear.
Check the destination before writing “defined above”.
For a definition involving a unitary design, identify the Hilbert-space dimension and the group carrying the Haar measure.
These choices determine the definition's mathematical setting.

Maintain a dependency list for notation.
Check it after moving or shortening sections.
Include figures, captions and tables because they can introduce a term before the body does.

**Check:** Trace each first use to a definition or a valid pointer.
A familiar name alone can still leave a manuscript-specific convention unspecified.

## E03. Give equations an explanatory role

Before an equation, state the question it answers.
After the equation, explain the consequence that matters for the argument.
Avoid a second prose transcription that repeats every symbol without explaining the result.

Use the same conventions when comparing methods.
In a gradient-cost comparison, identify the counted resource and precision target for every row.
Check model evaluations, measurement shots and elapsed time separately.
A compact table can expose different assumptions more clearly than disconnected formulas.

Include a small equation when it explains a mechanism better than a vague description.
A pairwise aggregation equation or a brief estimator definition can make a comparison understandable.
Keep the notation and assumptions consistent with the full construction.

**Check:** Can a reader explain why the equation appears here and what it establishes?

## E04. Build diagrams in the reader's learning order

Introduce wires, states, gates and measurement before a complex variational circuit when the audience needs those concepts.
Use small panels to connect an operation with its matrix or output.
Then assemble the feature loader, trainable layer and readout into the full model.
Adapt the starting point to the audience's prior knowledge.

Reuse a diagram when it directly supports the contribution's explanation.
Update its caption and references after moving it.
Preserve the scientific content and attribution.
A redraw needs a source comparison and a provenance record.

**Check:** Does each diagram assume only concepts that readers have already met or that its caption explains?

## E05. Give related terms explicit conditions of use

Create a terminology table with these fields:

| Field | What to record |
|---|---|
| Term | The name used in the manuscript. |
| Object | The mathematical or experimental object it names. |
| Definition | The precise meaning in this document. |
| Equivalent term | A proposed synonym or equivalent description. |
| Required conditions | Assumptions under which the equivalence holds. |
| Exceptions | Cases where the terms name different objects or properties. |

Use broad family names for broad claims.
Use precise names for representation and complexity claims.
Separate conservation laws, gate families, matrix representations and data symmetries.
Distinguish ordinary gates from controlled gates, and component layers from complete models.

**Synthetic example:** Two excitation-preserving gates can agree on an adjacent pair under a fixed mode order.
Their relation on distant modes or another subspace can require additional conditions.
Check connectivity, ordering conventions and the chosen subspace before asserting equivalence.
The example establishes no equivalence for an unspecified circuit family.

For reconfigurable beam splitter (RBS) and fermionic beam splitter (FBS) gates, record these conditions explicitly.
Verify the relation under the manuscript's own gate convention.

Verify each manuscript's equivalences against its own definitions and sources.
Keep established technical terms when a plain substitute would change their meaning.
Apply the author's preferred term consistently within its intended meaning.
Keep an established term such as “subspace” or “sequential parameter shift” when that meaning applies.
Preserve exact external titles and quoted terminology with the required attribution.
