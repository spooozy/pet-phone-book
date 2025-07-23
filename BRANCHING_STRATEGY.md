# BRANCHING_STRATEGY

Project uses a simplified [GitHub Flow Branching Strategy](https://docs.github.com/en/get-started/using-github/github-flow) with two branch types:
- Primary Branch:
    - `main` - the only permanent branch, representing the production-ready state at all times.
- Temporary Branches:
    - all other branches are temporary and created from main for specific work items.

## Key principles:
- `main` is always deployable - the code in it must pass all tests and be ready for production.
- Mandatory **Code Review** – all changes are included in main only through a Pull Request with approval from reviewers.
- Tests and CI are mandatory – before merging, PR must undergo checks (compiler checks, linters and tests).