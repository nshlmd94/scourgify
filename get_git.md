
# Git Reference Table

| Command                             | Purpose                                                                 |
|-------------------------------------|-------------------------------------------------------------------------|
| `git init`                          | Initializes a new Git repository                                        |
| `git status`                        | Shows the status of changes in the working directory                    |
| `git add filename`                 | Stages a specific file for commit                                      |
| `git add .`                         | Stages all changes (new, modified, deleted)                             |
| `git commit -m "message"`           | Commits staged changes with a message                                   |
| `git log`                           | Displays commit history                                                 |
| `git remote add origin URL`         | Adds a remote repository                                                |
| `git remote -v`                     | Verifies the remote URL                                                 |
| `git branch -M main`                | Renames the current branch to `main`                                    |
| `git push -u origin main`           | Pushes commits to the `main` branch and sets upstream                   |
| `git pull`                          | Pulls latest changes from remote repository                             |
| `git clone URL`                     | Clones an existing repository                                           |
| `git diff`                          | Shows changes between commits, commit and working tree, etc.            |
| `git checkout branch-name`          | Switches to a different branch                                          |
| `git checkout -b new-branch-name`   | Creates and switches to a new branch                                    |
| `git merge branch-name`             | Merges changes from the specified branch into current branch            |
| `git rm filename`                   | Removes a file from Git and working directory                           |
| `git reset --hard`                  | Resets the working directory to the last commit (DANGER: destructive)   |

# Tips

- Use `git status` often to know what's going on.
- Use `git log --oneline` for concise commit history.
- Use `git push` after every commit to keep GitHub up to date.