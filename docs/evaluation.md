# Evaluation record

Version 0.1.0 uses two original synthetic development cases.
They cover a false Gram-matrix claim and an inflated account of paired results.
Fresh assistants received the same input packets with and without the skill.
Both baseline outputs and both skill outputs corrected the mathematical and numerical errors.

The first reference contained a Gram-matrix example that overlapped the theorem exercise.
That example was removed before the two blind comparisons reported below.
The first blind reader slightly preferred the baseline on both cases.
The reader found a useful counterexample in the skill output's edit notes and unnecessary self-assessment language.
A focused revision kept explanatory content in the passage and review forms in working notes.
A fresh run followed that revision. A second blind reader again narrowly preferred the baseline on both cases.
The revised outputs addressed the specific placement and self-assessment issues.
They established no comparative gain in reader preference.
Later additions cover figure and proof presentation, author reasoning and baseline recovery.
Those additions received source-coverage review; matched behavioural trials have not tested them separately.

These are two development examples, with one response per condition and iteration.
They provide no held-out estimate of general writing quality or statistical evidence of improvement.
The evaluation did not measure automatic skill selection or live Claude-plugin discovery.
Token use and matched runtime telemetry were unavailable.
Human review remains pending.
The worked examples include the actual final passages and baseline responses for inspection.

The local distribution suite checks installation paths with spaces, repeated installation and existing conflicts.
It also checks platform consistency, document links and the reproducible data summary.
An independent code review exposed recursive inclusion of unlisted local files in release archives.
A failing regression reproduced that issue. The final package uses a reviewed per-file manifest.
The regression and a parent-path rejection check pass with the fix.
The official skill manifest validator accepts the canonical skill.
The installer and packaging helpers use the Python standard library.
The external manifest validator requires PyYAML.

The procedure also underwent a private development trial whose material is excluded from this repository.
An independent reader reported clearer argument and preserved evidence in that revision.
That qualitative result supplies no general performance estimate.
No private manuscript or source feedback forms part of the public release.
