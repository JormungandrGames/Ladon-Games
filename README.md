# 16-Bit-Hero-Arcade

###### Resources
* Visit http://pygame.org/docs/tut/newbieguide.html for a quick guide on pygames.
* For the pygames documentation http://www.pygame.org/docs/ under refrences you can find the api for pygames
* For a tutorial on how to make a game with pygames http://www.pygame.org/docs/tut/tom/MakeGames.html
* For moving images http://www.pygame.org/docs/tut/MoveIt.html
* Example of "Dirty Rectangle Processing" discussed in the pygames guide http://archives.seul.org/pygame/users/Apr-2006/msg00216.html
* For smooth gameplay http://gafferongames.com/game-physics/fix-your-timestep/

###### Workflow
1. Clone your fork to local computer:

	```
	git clone git@github.com:NAME/16-Bit-Hero-Arcade.git
	```
2. Add the master branch as the upstream

	```
	git remote add upstream git@github.com:cs360f16/16-Bit-Hero-Arcade.git
	```
3. Create a branch with this format

	```
	git branch puneid_bug/feature_issue
	```
4. Add and commit

	```
	git add .
	git commit -m "Message"
	```
5. Push branch to origin

	```
	git push origin BRANCH_NAME
	```
6. Send pull request from your fork

	```
	Go to branch and click "Pull Request"
	```
7. Wait for a team member to merge and fix any conflicts if there are any
	* For fixing merge conflicts, make a file for the fix and pull the branch down
	
		```
		mkdir issue_#
		cd issue_#
		git clone git@github.com:NAME/16-Bit-Hero-Arcade.git
		cd 16-Bit-Hero-Arcade

		git checkout -b punetid_issue_# master
		git pull https://github.com/NAME/16-Bit-Hero-Arcade.git puneid_issue_#

		fix conflicts

		git add .
		git commit -m "Message"

		git checkout master
		git merge --no-ff punetid_issue_#
		git push origin master
		```
8. After the pull request has been merged, on your local computer pull the changes down into you master and then push them to your fork

	```
	git checkout master
	git fetch upstream master
	git merge upstream/master
	```
9. You can now delete your branch

	```
	git branch -d punetid_issue_#
	```

### Dependencies
* Python2.7 Or newer
* Pygames

### Installing dependencies
##### Arch Linux
	```
	pacman -S python # For the lastest version of python
	pacman -S python2-pygame
	'''
##### Debian-Based Distros
	```
	# Comes with python 2.7, Upgrade with sudo apt-get install python3
	sudo apt-get install python-pygame # or visit http://packages.qa.debian.org/p/pygame.html
	```
##### Fedora-based Distros and Others
	```
	# Comes with python 2.7
	clone https://bitbucket.org/pygame/pygame
	python3 config.py
	python3 setup.py build
	python3 setup.py install
	```
### Running 16-Bit-Hero-Arcade
	```
	git clone https://github.com/cs360f16/16-Bit-Hero-Arcade.git
	cd 16-Bit-Hero-Arcade
	chmod u+x arcade.py
	./arcade.py
	```
### How to report Bugs or request Features
* Reporting Bugs can be done through submitting an issue, clearly marked as a bug with a description of how to replicate it
* Features may also be requested through submitting an issue, again, make sure it is marked as such

### User conduct
1. When submitting a pull request, another member shall merge it and fix any conflicts
2. We are following the PEP 8 -- Style Guide for Python Code, tags for what the object you are blit'ing are appreciated Ex. f_name for fonts or i_name for images

### License 
* GPL license

### Guide To developing 16-Bit-Hero-Arcade
1. Add a Game
	```
	### Items to check for
	* 
	```

	
