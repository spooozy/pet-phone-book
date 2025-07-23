# BRANCHING_STRATEGY

The project uses [GitHub Flow Branching Strategy](https://docs.github.com/en/get-started/using-github/github-flow).

## Main branches:
- `main` – a stable branch, always ready for deployment.
- `feature-*` – temporary branches for developing new features, fixes, and improvements.

## Key principles:
- `main` is always deployable - the code in it must pass all tests and be ready for production.
- Branches are created from `main` - each new task is done in a separate branch.
- Mandatory **Code Review** – all changes are included in main only through a Pull Request with approval from 3 reviewers.
- Tests and CI are mandatory – before merging, PR must undergo checks (compiler checks, linters and tests).


