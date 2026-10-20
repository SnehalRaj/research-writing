# Contribute

Start with a real failure or a concrete task the current skill handles poorly.
Describe the input, expected behaviour and protected scientific content.
Use material you may publish. Replace private artifacts with an original synthetic case.

Edit the canonical skill in `skills/research-writing/`.
Add a case before changing a rule. Keep the expected answer separate from the task input.
Record behaviour without the change, then repeat with the change.
If the baseline already passes, state that result.
Use a fresh reader for substantive revisions when possible.

Check scientific preservation before prose preference.
A phrase count alone cannot justify a rule.
Reject changes that remove assumptions, uncertainty or the explanation of a method.
Keep useful qualifications and accepted author choices.

Run the distribution tests and `python3 scripts/package.py --sync`.
Then run `python3 scripts/package.py --check`.
Update the changelog and version together for a release.
Add each intended release file to `release-files.txt` after review.
Files outside that manifest remain outside the release archive.
Review every public file and the Git history before publication.
Keep human author acceptance separate from a passing test.
