# Contributing to `Pet phonebook` project

This document was created for contributors in order to simplify the work for all participants. 

For quick navigation, use the [Table Of Contents](#table-of-contents).

## Table Of Contents

1. [Pull Request](#pull-request)
    - [How to make a PR](#how-to-make-a-pr)
    - [How to review a pull request](#how-to-review-a-pull-request)


## Pull Request

There's a long-term [branch](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) called `main`. It contains only a stable code. Stable code is a code that is ready to be released and passed all the quality gates (like compiler checks, code review process, tests). Only stable code should be added to PR.

### How to make a PR

Here is a step-by-step guide for creating a correct PR that is understandable to others. Follow the points clearly to avoid mistakes.

1. Make sure that there is a corresponding task on the board. If not, please make an issue with the following structure:
    - Clear and comprehensive title;
    - The description must include:
        - the "Why" section: explanation of the business needs (why do we need the task?);
        - the "What" section: task description, specific requirements or steps to complete the task.
    - Use proper labels if needed.
1. Assign task to yourself (including people who might work on the task).
1. Make a short-lived branch from the latest version of the `main` branch:
    ```bash
    git checkout -b <issue-number>-<name-of-the-branch>
    ```
    where:
    - `<issue-number>-<name-of-the-branch>` is the name of the newly created branch. The name of the branch must have the following format: words separated by dashes;
    - `<issue-number>` - number of the corresponding issue we're working on;
    - `<name-of-the-branch>` - description related to the title of the task. The description must describe the task that is being worked on in the current branch.
1. Work on the task and implement required changes.
1. We add the files that we want to offer to the pull request. The file name is specified instead of the <file> parameter.
    ```bash
    git add <file>
    ```
    where:
    - `<file>` - this is the name of the file whose changes are included in the commit.

1. Adding a comment to our PR. It is written instead of the <description of changes> parameter and contains a brief description of the changes in the file.
    ```bash
    git commit -m "<description of changes>"
    ```
    
1. We are sending a new branch with changes to the repository. 
    ```bash
    git push -u origin <issue-number>-<name-of-the-branch>
    ```

1. Moving on to our Github project.

1. After the git push, a green "Compare & pull request" button will appear on GitHub.
Clicking on it will open the PR settings.

    - Title - briefly describe the essence of the changes;
    - Description - this field must contain:
        - Detail what exactly was changed and why;
        - If the PR contains not a fully completed task, but a part of it, then write about the completed fragments. Then go back to the task card and use the checkboxes to mark what has already been completed (add checkboxes using markdown);
        - Specify a link to the task that PR is solving. It is more appropriate to do this at the beginning of the field. Writing `#<issue-number>`, then the link to the issue will be inserted automatically.

    - Assignee - Specific people responsible for working with PR. (usually the creator of the PR);
    - Labels - mark for the convenience of filtering (documentation/bug, etc.);
    - Projects - link PR to the project. With this, the PR card will appear on the task board;
    - Reviewers - select the people who will check PR. All team members should be indicated.

1. Before sending, check that the display is correct using the buttons "Write" and "Preview". Please correct any inaccuracies.

1. Click on the green "Create pull request" button.

1. After creating a PR, return to the task board. A card with a description of the new PR will appear in the "Backlog" column. Move it from the "Backlog" to the "In Review". Leave the task card in the "In Progress".

### How to review a pull request

A check is required before merging to protect the `main`. Request a [review on GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews) after creating PR.

If the reviewer missed a mistake, he bears the same responsibility for it as the creator of the PR.

1. Navigation 
    - Go to the repository tab on Github;
    - Click on the "Pull Request" button at the top. A tab will appear showing all PRs in the project;
    - Select PR by clicking on its name;
    - Go to the "Files changed" tab. All changes will be displayed here.
    
    By switching between the "Display the source diff" and "Display the rich diff" buttons, the file display format will change.

1. The PR verification stage:
    - Start checking the file for issues;
    - Actions when an issues is detected: 
        - Click on the "+" sign that appears after hovering over the line. If necessary, select several lines, hold down the button and pull down to the desired line;
        - Write a clear comment on the error. It is good practice to attach a screenshot;
        - Click "Add comment to review" to finalize the comment.

1. Completing the PR check:
    - Click on the "Finish your review" button;
    - Leave a general comment on this PR in the window;
    - Choose the final verdict for the review from the suggested ones:
        - Approve — the code is ready for installation;
        - Request changes — edits are required;
        - Comment — just leave a general comment without a verdict.

The 'Conversation' tab displays the full history of work on PR.
