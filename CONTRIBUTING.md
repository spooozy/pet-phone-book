## Branching Strategy

Project uses a simplified [GitHub Flow Branching Strategy](https://docs.github.com/en/get-started/using-github/github-flow) with two core branch types:
- Primary Branch:
    - `main` - the only long-lived branch, representing the production-ready state at all times. It contains only a stable code that passed all the quality gates (compiler checks, linters and tests). All changes in the `main` branch must be done via explicit PR and code review process.
- Feature Branches:
    - feature-branches are short-lived branches. They live until the moment when the work in the branch is merged into the `main`branch. Such branches and created from the `main` branch and must contain improvements/fixes that correspond to particular issue on the team's task board.

## How to make a PR

1. Make sure you have a corresponding task on the board. If not, please make an issue with the following structure:
    - Clear and comprehensive title;
    - The description must include:
        - the "Why" section: explanation of the business needs (why do we need the task?).
        - the "What" section: task description, specific requirements or steps to complete the task.
    - Use proper labels if needed.
1. Assign task to yourself (including people who might work on the task).
1. Make a short-lived branch from the latest version of the `main` branch:
    ```bash
    git checkout -b <issue-number>-<name-of-the-branch>
    ```
    
    where:
        - `<issue-number>-<name-of-the-branch>` is the name of the newly created branch. The name of the branch must have the following format: words separated by dashes. 
        - `<issue-number>` - number of the correponding issue we're working on.
        - `<name-of-the-branch>` - description related to the title of the task. The description must describe the task that is being work on in the current branch.
1. Work on the task and implement required changes.
