# Initial Setup
### Authentication
There are two main ways of authenticating with Git - SSH and PAT (Personal Access Token). In the interest of time, we will use a PAT.

### Config
Git requires you to configure your name and email before you can make commits. This can be done using the commands:
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```
The --global flag means this will be applied globally on your system, to every repo.

### Cloning Repo
```
git clone https://github.com/Aginic/traineeship-git-tutorial-2024.git
```

# Working on a ticket
For most clients (and internally in MG), your project management tool will be JIRA. However, we will be using GitHub Issues for this workshop to keep it simple. Please navigate to https://github.com/Aginic/traineeship-git-tutorial-2024/issues and have a read of the currently open tickets. After that, have a go at completing the tickets!

- Assign a ticket to you so that your teammates know you are working on it.
- Create a new feature branch for your ticket. A good format is <feature/feature_name>. E.g. `git checkout -b feature/update_read_me`
- Implement your ticket.
- Make a commit with your changes. Do this by:
    - Adding the files you want to include in your commit by adding them to the Stage. `git add <file>`
    - Once you have added all the files, it is a good idea to run `git status` to verify.
    - Make the commit by running `git commit -m "My commit message"`
- Push the changes to the Github repo by running `git push`. Please note that the first time you make a push, you may have to run `git push --set-upstream origin <branch_name>`.
- After the branch has been pushed, create a Pull Request (alternatively called a Merge Request on GitLab) from your branch to the main branch.
- Yell out in chat once this is done, and we will review and approve the PR together.
- After it has been approved, you can merge the PR. (Squash combines multiple commits into one, which can be ideal since you want a clean history.)
