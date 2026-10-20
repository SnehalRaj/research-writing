# Research Writing

Turn raw drafts, theorem statements and data into research articles that readers can follow.
The skill builds the argument, checks the evidence and revises the prose.

It grew from Snehal Raj's iterative PhD writing and review.
The public instructions generalise those lessons. The examples use original synthetic material.

## Install

Requires Python 3.10 or later for the installer. The writing skill itself uses your assistant's tools.
Clone or download this repository, then run one command from its root.
Choose the destination your installation uses for personal skills.

Codex:

```sh
python3 scripts/install.py --platform codex --dest "$HOME/.agents/skills"
```

Claude Code:

```sh
python3 scripts/install.py --platform claude --dest "$HOME/.claude/skills"
```

The installer preserves an existing different version.
To update, move the old skill directory aside and run the installer again.
Keep your local changes in that saved copy until you have reviewed the update.

The repository also contains a Claude plugin marketplace.
For a local checkout, use `/plugin marketplace add /absolute/path/to/research-writing`.
Then use `/plugin install research-writing@research-writing` and start a new session.
The plugin's skill files come from the same canonical source.

## Use

In Codex, invoke `$research-writing` with the task and source material.
In Claude Code, invoke `/research-writing` after a direct skill installation.
The plugin namespace is `/research-writing:research-writing`.

> Revise this complete article for clarity and connected reasoning. Preserve the numerical results and scientific assumptions. Give me the revised source, a PDF and a short change record.

The skill also handles raw results and theorem drafts.
For a local wording change, it uses a short route.
It keeps scientific checks, editorial review and author acceptance separate.

## Examples

- [A Gram-matrix theorem](examples/gram-matrix/README.md): an incorrect guarantee becomes a precise, useful result.
- [Paired experimental results](examples/paired-results/README.md): raw counts become a correctly scoped results passage.

Each example contains the raw draft, the evidence, the revision and the important decisions.

## Development

Edit `skills/research-writing/` first.
Then run:

```sh
python3 scripts/package.py --sync
python3 -m unittest discover -s tests -v
python3 scripts/package.py --check
```

To create a release archive outside the repository:

```sh
python3 scripts/package.py --archive ../research-writing.zip
```

The archive includes only the reviewed paths in `release-files.txt`.
Review [the contribution rules](CONTRIBUTING.md) before changing the skill.
[Evaluation](docs/evaluation.md) records the checks and their limits.
[Sources](docs/sources.md) explains the method's origin and external references.

## Status

Version 0.1.0 is an initial release candidate.
It includes portable instructions, two worked examples and local distribution checks.
User review determines whether a revised article meets its purpose.
