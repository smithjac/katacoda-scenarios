# Configuration

Before we get into working in a repository we have to make sure we have our system configured correctly. You must first configure Git correctly and then create a personal access token on GitHub. This step will guide your through this process.

### Configuring Git
When you configure Git, this is how your peers will see who has made changes to the repo and what changes they made. First, copy this command  `git config --global user.email `{{copy}} and add your email that is used with your GitHub account. Then run this command in the terminal provided so the email is configured correctly. Then, copy this command `git config --global user.name `{{copy}} and add your name. This will be displayed to anybody that has access to the repository you are working in.

### Configuring GitHub Personal Access token
GitHub recently required that before connecting to GitHub through the command line, you must authenticate your account by using a personal access token. If you do not yet have a token these are the steps you need to follow to create one.

Sign into your GitHub account through your web browser and in the top right corner of the window you'll see your profile picture for your account. Click on this and you'll see 'Settings' at the bottom of the dropdown menu. Click on this and it should redirect you to a page where you can make changes to your account. If you scroll down you will see on the left side of the screen a button titled 'Developer Settings', click on this and you'll then see three more options on the left. Choose 'Personal Access Tokens'. Towards the middle of the screen choose 'Generate new token', this may ask you to enter your password for your account. After entering your password you can now create the token you will be using to communicate to GitHub through the command line. For the note just enter something along the lines of 'Command Line Interface'. For the list of boxes in the middle of the page, only click the boxes labeled 'repo' and 'delete_repo'. It is standard practice to give as little amount of privileges as you need for security reasons. Scroll down and click the 'Generate token', your personal access token will be displayed. Make sure you copy this to your clipboard and save this token or you will not be able to interact with the repository on GitHub. Keep this token safe, it is private and should not be shared with others.

After completing these steps
