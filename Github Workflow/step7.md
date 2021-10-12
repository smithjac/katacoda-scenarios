# What's the Conflict?

A conflict occurs when your origin repo is out of date with the upstream repo and you made changes to lines of code that are out of sync with upstream. In order to resolve this we must get the latest code from upstream and implement both your change and the change that was already approved.

# Pull from Upstream

Go to the upstream repo on GitHub and you will see a green button towards the middle of the screen that reads 'Code'. Click this and a drop down menu will appear with an option to get an HTTPS link and copy it to your clip board. If you remember, this is similar to when we first cloned our origin repo to work locally. Although this will be a little different than before. Go to the terminal to execute the command `git remote add upstream `{{copy}}, put the link that you copied at the end of the command and hit enter. Your local repo now contains the updated code that was accepted into the main branch after you originally forked.
