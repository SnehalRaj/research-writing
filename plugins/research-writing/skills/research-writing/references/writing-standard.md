# Writing standard

This is the author's writing profile. Apply it when the user asks for this style.
Use another author's explicit brief when that brief differs.
The sentence limits below form a local simplified-English profile.
They do not certify compliance with the complete ASD-STE100 standard.

## Orwell's six rules

1. Never use a metaphor, simile, or other figure of speech which you are used to seeing in print.
2. Never use a long word where a short one will do.
3. If it is possible to cut a word out, always cut it out.
4. Never use the passive where you can use the active.
5. Never use a foreign phrase, a scientific word, or a jargon word if you can think of an everyday equivalent.
6. Break any of these rules sooner than say anything outright barbarous.

## The author's 2026 additions

7. Ban corrective juxtaposition: the “not X, it is Y” shell and its variants. State the supported claim directly.
8. Two examples are enough. Do not stretch to three.
9. Say the point directly. Remove announcements about what follows.
10. Do not end two paragraphs in a row with punchlines.
11. Vary the length and shape of neighbouring sentences.
12. Break any of these rules sooner than write like a machine.

The example limit concerns decorative examples. Retain all distinct contributions and necessary scientific cases.
The ban in rule 7 covers rhetorical correction. Preserve factual negation, counterexamples and necessary comparisons.
Use no em dashes. Use an en dash to join proper names when the naming convention requires it.

## Simplified English and Zinsser

- Give each sentence one idea. Give each instruction one action.
- Keep procedural sentences to 20 words or fewer. Keep descriptive sentences to 25.
- Use the active voice. Name the actor.
- Give each term one meaning. Repeat the term when a synonym would obscure it.
- Prefer a simple verb form. Replace an “-ing” phrase when a plain verb says the same thing.
- Use no noun cluster longer than three words. Expand a long cluster into a phrase with clear relations.
- Keep the articles. Retain “the” and “a” when the grammar needs them.
- Write positive instructions. Tell the reader what to do.

Zinsser's four principles guide each choice:

| Principle | Editorial action |
|---|---|
| Simplicity | Strip each sentence to its cleanest components. |
| Brevity | Cut words that add no meaning. |
| Clarity | Supply the explanation that the reader needs. |
| Humanity | Write like a person, to a person. |

Keep necessary conditions even when they make a sentence harder to shorten.
Split a long statement at a logical boundary. Check that the new sentences retain the same claim.
Read the whole paragraph after a local edit. Short sentences still need an explicit relation.

## Scientific register

Use established terms from the literature. Define a term before it carries part of the argument.
Keep qualifiers that change meaning: “approximately”, “asymptotically”, “in expectation” and “under this noise model”.
Keep a scientific passive when its object is the relevant topic and the actor is already clear.
Prefer an active construction when attribution matters.
An algorithm may compute and a bound may imply. These verbs name exact relations.
Check personification when it hides the actual process or actor.

Use verbs that identify the work:

| Purpose | Verbs and checks |
|---|---|
| Define or design | Define, construct. Name the object and its assumptions. |
| Calculate | Compute for an exact operation; estimate for an uncertain quantity. |
| Run an experiment | Train, evaluate. Name the data, model and metric. |
| Compare | Compare, test. Name the baseline and the test. |
| Report evidence | Find, show. Preserve the tested population and range. |
| Establish a formal result | Prove, derive. Point to the proof or derivation. |
| Explain an operation | Apply, measure. Name the operation and its object. |
| State a constraint | Preserve, require. Name the property or condition. |

This vocabulary is a guide. Check “supply”, “enable”, “provide” and “fixes” when they hide the action.
For example, a setting specifies parameters and a unitary preserves a subspace.
Keep technical uses such as “fixed depth”.

## Detailed checks for AI writing tics

Inspect these patterns in context. A search flag starts a review; it cannot establish poor writing.

| Pattern | What to check and repair |
|---|---|
| Throat clearing | Remove “Here's the thing”, “The truth is” and similar openings. State the subject. |
| Empty emphasis | Replace “crucially”, “importantly”, “fundamentally” and “Let that sink in” with the actual consequence, if one exists. |
| Vague significance | Name the implication instead of calling it significant, deep or transformative. |
| Promotional language | Replace “game changer” and “groundbreaking” with the result and its comparison. |
| Business metaphors | Replace “navigate”, “landscape”, “deep dive” and “moving forward” when they obscure a technical action. |
| Corrective shells | Remove binary corrections, negative listing and repeated “not just” constructions used for emphasis. |
| Dramatic fragments | Join isolated nouns and punchlines into complete explanatory sentences. |
| Rhetorical setups | Remove a question followed by a staged answer when a direct statement gives the same information. |
| Empty narration | Cut “In this section we will” when the heading and opening already establish the purpose. |
| False agency | Name the mechanism behind claims such as “the data tells us” or “the decision emerges”. |
| Distant narrator | Replace claims about what “nobody” knows or what “everyone” does with evidence and a defined population. |
| Unjustified extremes | Check every “always”, “never”, “first” and “all” against its quantifier and source. |
| Mechanical rhythm | Read adjacent sentences for repeated openings, lengths and shapes. Vary them without fragments. |
| Repeated endings | Check adjacent paragraphs for successive slogans, summaries or punchlines. |
| Redundant examples | Retain examples that resolve distinct reader difficulties. Cut decorative repetition. |
| Stock transitions | Use “therefore” only for an implication and “because” only for a supported reason. Supply missing reasoning. |

Older source notes used blanket bans on adverbs, nonhuman subjects and Wh-word openings.
Apply the scientific distinctions above. Preserve genuine research questions and useful conditional sentences.
The pattern catalogue draws on the author's supplied Stop Slop notes.
Its academic adaptation avoids copying the source's examples and numerical scoring threshold.

## Openings, definitions and paragraph flow

Name the central subject in a heading. A paired heading needs a section about that relationship.
Open with the context, problem or principle that gives the section a purpose.
Introduce the model before its blocks. Explain a method's role before its update rule.
Give a new term its own defining clause or sentence.
Use `\emph{term}` at an inline definition's first occurrence when the author uses this convention.
Use a formal definition when the paper needs an exact reusable statement.

Give each paragraph a reader question. Explain how its sentences answer that question.
Treat “reads like a list” as a possible failure of reasoning links.
Choose a list when the reader must compare separate items or follow steps.
Explain why an example appears and what the equation establishes.
See [exposition rules](rules/02-exposition-and-terminology.md) and [author style](author-style.md).

## Figures, endings and local conventions

State the scientific point before citing its figure. Put panel and colour descriptions in the caption when possible.
Keep labels readable at the intended page size. Check float order and gaps in the rendered output.
State a result before the concrete next study. Name what future work would test and why.
Keep limits that follow from the metric or theorem in the explanation itself.
Avoid a generic disclaimer after every result.

The following conventions are optional. Apply them when they match the author's brief.
For first-person plural, use “we”, “our” and “us” consistently.
Use “quantum machine learning” in headings and prose when the author prefers that term.
Preserve exact published titles when citing external works.
When quantum advantage is a research goal, use “seeks” to describe that goal.
Preserve the evidence status of each advantage claim.
One possible convention places a contribution chapter's main figure at the top of its second page.
Choose figure placement from the document's format and argument.
Group related work by ideas. About one page can serve as an initial target for a related-work subsection.
Set article length targets from the venue and the comparison the reader needs.
One conclusion order starts with the contributions and their evidence.
It then relates them to prior work, states limits and names useful next studies.
For a chapter, the ending can connect earlier chapters, the present contribution and questions that later chapters take up.
Use this order when it fits the document's role.
Present the author's contribution directly while preserving collaborator roles and source credit.
Use self-citations where omitted details make them useful. Keep full provenance in working notes.
For LaTeX source, 80-column wrapping can make review locators precise.
Preserve commands, comment markers and verbatim blocks during wrapping.
Check that a whitespace-only format pass preserves the rendered text.

## Conflicts and authority

| Older instruction or tempting shortcut | Current treatment |
|---|---|
| Keep sentences broadly even in length. | Apply the author's later rule for varied neighbouring sentences. Preserve complete sentences. |
| Remove all adverbs and passive clauses. | Remove empty emphasis. Preserve scientific meaning and clear attribution. |
| Copy an admired writer's phrasing. | Study the order of ideas. Use the current author's facts and voice. |
| Repeat one claim verbatim throughout. | Keep the central claim consistent. Let each section develop its own part of the argument. |
| Add a roadmap or explicit question to every opening. | Fulfil the reader's needs. Use the form that fits the section and current brief. |
| Treat a low style score as rejection. | Report the exact fault and its consequence. Author acceptance remains separate. |
| Drafting requires fresh permission at every step. | Follow the scope already authorised. Record the exact unit and version accepted. |

