# Build the research argument

Apply these rules after the sources, contribution candidates and dependencies have an evidence record.
Use the [method](../method.md) to establish that preparation.
The examples below are synthetic teaching examples.

## N01. Give the reader a question worth answering

State the practical or scientific difficulty that makes the contribution useful.
Then explain what the proposed method changes.
Keep the research question distinct from the method's definition.
A description of an operation alone can leave the reason for studying it unclear.

**Synthetic example:** A model freezes most weights during adaptation.
That description leaves the quality-cost question open: how much can the trainable parameter count fall while task performance remains useful?
An estimator comparison likewise needs a reason to compare estimators before its variance analysis begins.

**Check:** Can a reader explain what would remain difficult without the proposed method?
The answer should identify the problem and the contribution's intended role.

## N02. Give each paragraph one job and each transition a reason

Map a paragraph as a question, answer, supporting evidence and implication.
Some paragraphs need only two of these parts.
Use the parts that the paragraph's job requires.
Vary the form when the reasoning needs a different order.

For each sentence, name its relation to the previous one.
Possible relations include explanation, example, consequence, qualification and next step.
Write the missing reason when the relation is unclear.
Use a connector such as “because” or “therefore” when the evidence supports that relation.
A connector alone cannot repair missing reasoning.

A reviewer may call disconnected prose a list.
Inspect how the sentences connect before changing the format.
Use a list when readers need independent choices or procedural steps.

**Deletion test:** Remove a sentence provisionally.
If the argument loses nothing, give the sentence a distinct purpose or cut it.
A striking fact in an opening still needs a role in the research question.

## N03. State the author's research choice

Ask the author to explain a difficult passage aloud when their reasoning remains unclear.
Capture the problem, chosen approach and reason for that choice.
Preserve those reasons during compression.
Use an existing account when it already supplies them.

**Synthetic example:** A study combines a theoretical model, simulations and selected hardware tests.
Explain which model choices the experiments examine and why their behaviour was hard to predict in advance.
That reason gives the account of the research process a scientific purpose.
A list of the tools alone leaves the choice unexplained.

Label a research position as a choice or interpretation when appropriate.
“We choose” and “we investigate” can state that position clearly when they fit the manuscript's voice.
An interpretation still needs accurate facts and a defensible inference.

**Check:** Can a reader explain why the authors chose this approach?
Compare the compressed account with the recorded reasons.

## N04. Recall the background that the current argument needs

Give a contribution chapter enough context for an independent reading.
Recall a concept through its present role, then point to its earlier definition.
A brief recap of message passing can explain why a new graph construction takes its form.
The recap should connect the background to the contribution.

Place shared definitions in the background when several chapters use them.
Include a full derivation when readers need it to understand or check a later result.
Use citations and cross-references to reduce repetition while retaining the reasoning needed in the current passage.

**Check:** Follow every background pointer as a reader.
Confirm that it reaches the required concept and that the current explanation remains understandable.

## N05. Lead with the supported result

State what improved, what was established or what was learned before listing experimental settings.
Keep the task and comparison scope beside the result.
Strong performance and a small parameter count can lead the account when the evidence supports both.
Name the tasks and compared methods that make the statement true.

Separate predictive performance from agreement between a hardware experiment and a simulation.
Each answers a different scientific question and needs its own evidence.

A failed objective can support a useful result.
**Synthetic example:** An optimisation loss improves while held-out performance does not.
Explain how that finding motivates a specified change to the objective or a model that uses the data distribution.
Preserve the failure and the status of the proposed change.

**Check:** Does the result sentence state the finding, evidence type and comparison needed for its interpretation?

## N06. Make the ending answer the opening

Use the current research questions when writing the conclusion.
State the contribution, its evidence and what follows for the wider problem.
Check the introduction again after those questions change.
A conclusion should answer the questions that the document now asks.

Keep one useful roadmap at each level where readers need navigation.
A chapter map and a thesis map serve different reading tasks.
Repeated research questions can help a conclusion answer them explicitly.
Judge each repetition by its role and the author's decision.

For a thesis chapter, explain relevant links to earlier work and the questions that later chapters take up.
Use chapter references when they help the reader follow that connection.
Other sections should stay focused on their own purpose.

**Paper use:** Select one central question and a small set of supporting contributions.
Build the paper's case through its problem, prior work and evidence.
Use the [paper adaptation](07-adapting-the-method-to-papers.md) when the thesis sequence no longer supplies the structure.
