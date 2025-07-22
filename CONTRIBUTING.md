There's a long-term branch called `main`. It contains only a stable code. Stable code is a code that is ready to be released and passed all the quality gates (like compiler checks, code review process, tests).

## How to make a PR

1. Make sure you have a corresponding task on the board. If not, please make an issue with the following structure:
    - Clear and comprehensive title;
    - The description must include:
        - the "Why" section: explanation of the business needs (why do we need the task?)
        - the "What" section: task description, specific requirements or steps to complete the task.
    - Use proper labels if needed;
1. Assign task to yourself (including people who might work on the task)
1. Make a short-lived branch from the latest version of the `main` branch:
    ```bash
    git checkout -b <issue-number>-<name-of-the-branch>
    ```
    where:
        - `<issue-number>-<name-of-the-branch>` is the name of the newly created branch. The name of the branch must have the following format: words separated by dashes. 
        - `<issue-number>` - number of the correponding issue we're working on.
        - `<name-of-the-branch>` - description related to the title of the task. The description must describe the task that is being work on in the current branch.
1. Work on the task.
