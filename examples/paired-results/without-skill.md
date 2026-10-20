## Research passage

We compared the candidate and baseline on one synthetic classification task using five matched training seeds. Both methods used the same split and training budget. Each run used the same fixed held-out set of 100 items.

Mean accuracy across seeds was 73% for the candidate and 72% for the baseline, a gain of 1 percentage point. The paired differences were +2, +1, −1, +2, and +1 percentage points. The candidate improved accuracy on four seeds and reduced accuracy on one. The sample standard deviation of the paired differences was 1.22 percentage points.

These results describe variation across training seeds on this fixed held-out set. They provide no estimate of variation across test sets or tasks. No significance test was specified, and the supplied counts do not establish statistical significance. The available data also provide no comparison of runtime or resource use.

## Edits and calculations

- Each correct prediction contributes 1 percentage point because every run evaluates 100 items. Baseline counts sum to 360; candidate counts sum to 365. Dividing each sum by five gives mean accuracies of 72% and 73%.
- The paired differences sum to 5 percentage points. Their mean is 1 percentage point. Their sample standard deviation is \(\sqrt{6/4}=1.2247\) percentage points, using five paired seeds.
- Replaced the claimed 10% improvement with a 1 percentage point gain. Relative to the baseline mean, the gain is \(100(73-72)/72\approx1.39\%\).
- Removed claims of consistent gains, statistical significance, lower resource costs, and generalisation across tasks. The five seeds share 100 test items, so the experiment does not contain 500 distinct test items. The supplied aggregate counts also cannot recover paired outcomes for individual items.
