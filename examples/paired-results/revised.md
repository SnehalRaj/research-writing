## Research passage

On one synthetic classification task, the candidate averaged 73% accuracy across five matched training seeds, compared with 72% for the baseline. Both methods used the same split and training budget. Each run used the same held-out set of 100 items.

The mean gain was 1 percentage point, or about 1.39% relative to the baseline. The candidate improved in four seeds and lost one percentage point in the remaining seed. The paired changes ranged from −1 to +2 percentage points. These results show a small mean accuracy gain on this task and held-out set. They leave statistical significance and performance across tasks unresolved. The supplied measurements provide no evidence of reduced resource use.

## Edits and calculations

I calculated each run's accuracy as its correct count divided by 100. The seed means are

\[
\bar A_{\mathrm{baseline}}
=\frac{71+72+70+74+73}{5\times100}
=0.72,
\]

\[
\bar A_{\mathrm{candidate}}
=\frac{73+73+69+76+74}{5\times100}
=0.73.
\]

The paired changes, in seed order, are \((2,1,-1,2,1)\) percentage points. Their mean is \(1\) percentage point. The relative gain is \((0.73-0.72)/0.72\times100\approx1.39\%\). The denominators above count 500 evaluations across repeated runs on the same 100 items.

- Replaced the draft's “10%” improvement with the verified absolute and relative gains.
- Replaced “consistently and significantly outperforms” with the mean gain and the observed variation across paired seeds. No significance test or equivalence margin was specified, so I made no significance or equivalence claim.
- Removed the claims of reduced resource costs and superior generalisation across tasks. The supplied files contain no resource measurements or additional tasks. They also contain no per-item predictions.
- Preserved the shared split, equal training budget, five matched seeds and fixed test set. The repeated runs describe variation across these training seeds on that set.

I verified the counts, means and paired differences with Python using exact fractions. The source fidelity, descriptive calculations, argument and exposition pass the review. I checked the Markdown and equations in source; rendered presentation remains unchecked. Author acceptance is pending.
