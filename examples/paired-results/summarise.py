"""Reproduce the descriptive summary for this synthetic experiment."""
import csv
import json
import statistics
from pathlib import Path


def summarise(path):
    with path.open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    if not rows:
        raise ValueError("The results file has no observations.")
    baseline, candidate = [], []
    for row in rows:
        total = int(row["test_items"])
        first, second = int(row["baseline_correct"]), int(row["candidate_correct"])
        if total <= 0 or not (0 <= first <= total and 0 <= second <= total):
            raise ValueError("Prediction counts must fit a positive test-set size.")
        baseline.append(first / total)
        candidate.append(second / total)
    differences = [(b - a) * 100 for a, b in zip(baseline, candidate)]
    mean_baseline, mean_candidate = statistics.mean(baseline), statistics.mean(candidate)
    return {"seeds": len(rows), "baseline_mean_accuracy": mean_baseline,
            "candidate_mean_accuracy": mean_candidate,
            "paired_difference_percentage_points": differences,
            "mean_difference_percentage_points": statistics.mean(differences),
            "sample_sd_difference_percentage_points": statistics.stdev(differences) if len(rows) > 1 else None,
            "relative_gain_percent": 100 * (mean_candidate - mean_baseline) / mean_baseline if mean_baseline else None,
            "seeds_improved": sum(x > 0 for x in differences),
            "seeds_worsened": sum(x < 0 for x in differences)}


if __name__ == "__main__":
    print(json.dumps(summarise(Path(__file__).with_name("results.csv")), indent=2))
