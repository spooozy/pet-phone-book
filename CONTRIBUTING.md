## Contributing to Pet Phone Book

The following is a set of guidelines for contributing to Pet Phone Book. 

## Table Of Contents

1. [Code of Conduct](#code-of-conduct)
1. [Documentation](#documentation)
1. [Pull Request](#pull-request)
    - [How to make a PR](#how-to-make-a-pr)
    - [How to review a pull request](#how-to-review-a-pull-request)
1. [Reporting Bugs](#reporting-bugs)
1. [Styleguides](#styleguides)
1. [License](#license)

_in Progress|being considered_
1. Repository structure
1. Local Setup


## Code of Conduct
The following points were suggested for more comfortable communication. This is not a direct requirement, but a recommendation.
- Maintain communication without using [meta questions](https://nometa.xyz/);
- Answer questions from teammates;
- Be able to accept constructive criticism;
- Using friendly language;
- Strive for a sufficient level of self-reflection;
- If possible, turn on the camera on Google Meet.

## Documentation

- [Feature set](https://docs.google.com/document/d/1_v17UpmBQqAdpPxYHHrB2L2zC9Md2PzVwXfs-eDycMw/edit?usp=sharing);
- [Architecture description](https://docs.google.com/document/d/1bkvN1lTqco-4gUwVz_hfJ2CP0F3HoiRH3OQeBf-RiA8/edit?usp=sharing);
- [README.md](https://github.com/dersim-davaod/pet-phone-book/blob/main/README.md);
- [CONTRIBUTING.md](https://github.com/dersim-davaod/pet-phone-book/blob/main/CONTRIBUTING.md);
- [BRANCHING_STRATEGY.md]().

## Pull Request

There's a long-term branch called `main`. It contains only a stable code. Stable code is a code that is ready to be released and passed all the quality gates (like compiler checks, code review process, tests).

### How to make a PR

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
    - `<issue-number>` - number of the corresponding issue we're working on.
    - `<name-of-the-branch>` - description related to the title of the task. The description must describe the task that is being worked on in the current branch.
1. Work on the task and implement required changes.
1. We add the files that we want to offer to the pull request. The file name is specified instead of the <file> parameter.
    ```bash
    `git add <file>`
    ```

1. Adding a comment to our PR. It is written instead of the <description of changes> parameter and contains a brief description of the changes in the file.
    ```bash
    `git commit -m "<description of changes>"`
    ```
    
1. We are sending a new branch with changes to the repository. 
    ```bash
    `git push -u origin <issue-number>-<name-of-the-branch>`
    ```

    You can also add the '-u` flag. It allows you to pin this branch so that you don't have to write the full name of the branch every time.

1. Moving on to our Github project.

1. After the git push, a green "Compare & pull request" button will appear on GitHub.
Clicking on it will take you to the PR settings.

    - Title - briefly describe the essence of the changes;
    - Description - detail what exactly was changed and why;
    - Assignet - Specific people responsible for working with PR. (usually the creator of the PR);
    - Labels - mark for the convenience of filtering (documentation/bug, etc.);
    - Projects - link your PR to the project. This will help you keep track of your tasks;
    - Reviewers - select the people who will check your PR before meeting.
    
1. Click on the green "Create pull request" button.

### How to review a pull request

1. Navigation 
    - Go to the repository tab on Github;
    - Click on the "Pull Request" button at the top. When you click on it, a tab will appear with all the PR that is in the project;
    - Select your PR by clicking on its name;
    - Go to the "Files changed" tab. Here you will see all the changes.
    
    You can also view the file by switching between "Display the source diff" and "Display the rich diff".

    **In our project, we specify the entire team as reviewers.**

1. The PR verification stage:
    - Start checking the file for errors;
    - If you notice a mistake: 
        - Click on the "+" sign that appears after hovering over the line. If you need to select several lines, then hold down the button and pull it down;
        - Write a clear comment on the error. It is good practice to attach a screenshot;
        - After you finish commenting, click on the "Add review comment" button.

1. Completing the PR check:
    - Click on the Finish your review button.";
    - Leave a general comment on this PR in the window;
    - Choose the final verdict for the review from the suggested ones:
        - Approve — the code is ready for installation;
        - Request changes — edits are required;
        - Comment — just leave a general comment without a verdict.

You can view the history of your work on PR by clicking on the "Conversation" tab.



## Reporting Bugs

If you notice an error during development/operation, you should inform the team about it. In order to write a competent message, analyze the error and describe it in these points:
- Use a clear name of the problem to identify it;
- Describe the exact steps that led to this error;
- Attach specific examples: links to files, code snippets, etc;
- Describe the eating that you saw after completing the steps that led to the error;
- Describe the behavior that should have happened during these steps.


## Styleguides
- Use the present tense ("Add feature" not "Added feature")

_in Process:_
- JavaScript Styleguide
- Documentation Styleguide (use Markdown)


## License


_there will be a link to LICENSE.md and a brief explanation_

