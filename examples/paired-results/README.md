# From counts to a readable results passage

This is an original synthetic exercise. It describes no real model or dataset.
Read [the raw draft](raw.md), [the data](results.csv) and [the revised passage](revised.md).
The final passage came from an independent assistant run with the skill.

The methods share one test set and five matched training seeds.
Mean accuracy is 72% for the baseline and 73% for the candidate.
The gain is one percentage point, or about 1.39% relative to the baseline mean.
The candidate improves on four seeds and performs worse on one.

Run the supplied calculation from the repository root:

```sh
python3 examples/paired-results/summarise.py
```

The revision removes the unsupported claims of statistical significance and lower resource cost.
It preserves the scale and direction of the observed difference.
The fixed test set limits the interpretation of variation across seeds.
The available counts do not supply independent outcomes for 500 test items.

A fresh baseline assistant also corrected this example without the skill.
The example demonstrates the transformation from data to a supported passage.
It provides no estimate of general improvement across scientific writing.
