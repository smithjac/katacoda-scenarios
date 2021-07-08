# Making Changes Locally

In this step, we will learn the basic skills of forking and cloning from GitHub. We will also learn how to make changes to that repository locally without it affecting the repositories on GitHub.

### Fork and Clone

First, we need to fork the main repo from GitHub which we will refer to as 'upstream'. To do this you must go to GitHub and press the fork button in the top right of the screen. You can then choose the location of where you would like to fork it to. We will now refer to this forked repo as 'origin'. Once you have it forked go to 'origin' and click on the green button that reads 'Code'. After that you can click the clipboard where it will be copied.

Next, you will go to the terminal and type 'git clone (insert copied link here)'. This will clone the directory structure of your repo so you can make changes locally, without it affecting either 'upstream' or 'origin'. But before we make any changes, we have to first checkout a new branch.

### Checkout a Branch

Whenever you would like to make a change in a git repository, it is always good practice to do your work in separate branches. This helps to create a clean, organized repository structure and makes it easier for other team members to collaborate on projects. We will be making a simple change that involves adding a contributor to the README.md file. To do this we must go to the terminal and type `git checkout -b 'contributor'`{{execute}} which creates and switches you to a branch called 'contributor'. Now we are ready to make changes to our repository.

### Editing a File

Use the text editor provided to just add your name to the contributor's section of the README.md file. After your change is made, git will recognize the file being edited. To see this, type `git status`{{execute}} in your terminal and the file will say it has been edited but not added to the commit stage yet.

### Staging a File

We are ready to add the file to be part of the next commit in our repository. To do this, we must type `git add README.md`{{execute}} in your terminal. If you type `git status`{{execute}} again, you will now see that it has been staged and is a part of the next commit. If you did not mean to add the file quite yet, you can reset the staging area by typing `git reset`{{execute}} in the terminal and the file will still be edited but not staged.

### Making a Commit

Now that your edited files have been added to the staging area, you can commit these new features by typing `git commit -m "Added a contributor"`{{execute}}. You can see each of your commits by typing `git hist`{{execute}} into your terminal and it will also show each message for each commit. Using 'git hist' will also show the repository structure for each of your branches and wherever there is a merge. 
