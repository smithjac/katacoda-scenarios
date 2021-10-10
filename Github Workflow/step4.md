# Working Locally

You should now have a directory labeled the same name as the repository you cloned from. In order to work in this repository we must navigate into the directory by executing `cd `{{copy}} then add the name of the repo to the end of the command and hit return.

### Creating a Branch

Whenever you would like to make a change in a git repository, it is always good practice to do your work in separate branches. This helps to create a clean, organized repository structure and makes it easier for other team members to collaborate on projects. We will be making a simple change that involves adding a contributor to the README.md file. To do this we must go to the terminal and type `git checkout -b 'grammar'`{{execute}} which creates and switches you to a branch called 'contributor'. Now we are ready to make changes to our repository.

### Make the Change

In this example, we just want to change the 'Push' in fifth bullet point to 'push' and change 'Pull Request' to 'pull request' in the sixth bullet point. Typically you would be making a change to some code that has a larger impact than a grammar change although it is not uncommon to make small changes like this.

### Stage the File

Git will recognize whenever you make a change to a file. You can see this by executing `git status`{{execute}} at the command line. The file "README.md" will be labeled as modified although it is not staged to be a part of the next commit. In order to make sure this change will go into affect we have to add it to the staging area by executing `git add README.md`{{execute}} at the command line. If we execute `git status`{{execute}} again we will see that the file is in fact staged for the next commit.

### Making a Commit

In order to get our updated code to our repo on GitHub, we first have to commit the changes in our local repo. To do this, we execute the command `git commit -m 'Fixed grammatical errors in bullet points'`{{execute}} in the terminal. The '-m' option is just to specify the message you would like displayed when looking at the history of the repo.
