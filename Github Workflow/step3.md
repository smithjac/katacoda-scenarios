# Clone a Repo

There are three different ways you can clone a repo that GitHub provides. You can use an HTTPS link, an SSH key, or use their CLI. In this scenario we will be learning how to clone using the HTTPS link they provide.

### How to Clone a Repo

Go into the repo you forked in the previous step and you should see that the repo only has a README.md file that was added by another user. Towards the right side of the screen there is a green 'Code' button. Click on this and it will display a dropdown menu. By default it will open to the HTTPS link which is what we will be using. There will be a button on the right side of the dropdown menu that looks like a square stacked on another square. Click this and it will copy the link to your clipboard. Now make your way to the terminal provided in the scenario and type this command `git clone `{{copy}} and then paste the link right after clone. Then hit return and you'll see that git displayed some output to the screen. Execute `ls`{{execute}} and you should see that the name of the repo is now in your current directory.

Congratulations, you are now ready to start making changes to your repo locally.
