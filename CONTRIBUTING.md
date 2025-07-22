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
- `<issue-number>-<name-of-the-branch>` is the name of the newly created branch, слова в названии указывать через дефисы.
- `<issue-number>` - number of the correponding issue we're working on.
- `<name-of-the-branch>` - описание задачи близкое к тайтл соответствующей задаче на борде; должно описывать задачу, которая решается в данной ветке
1. Work on the task.
