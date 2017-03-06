# Ladon-Games

###This was completed through a Computer Science course at 
Pacific University (https://www.pacificu.edu/future-undergraduates/academics/areas-study/computer-science) 
taught by Dr. Chadd Williams (http://zeus.cs.pacificu.edu/chadd/)

###### Resources
* Visit http://pygame.org/docs/tut/newbieguide.html for a quick guide on pygames.
* For the pygames documentation http://www.pygame.org/docs/ under refrences you can find the api for pygames
* For a tutorial on how to make a game with pygames http://www.pygame.org/docs/tut/tom/MakeGames.html
* For moving images http://www.pygame.org/docs/tut/MoveIt.html
* Example of "Dirty Rectangle Processing" discussed in the pygames guide http://archives.seul.org/pygame/users/Apr-2006/msg00216.html
* For smooth gameplay http://gafferongames.com/game-physics/fix-your-timestep/

### Dependencies
* Python2.7 Or newer
* Pygame
	- Should you have any issues with starting 16-Bit-Hero-Arcade, change the following lines:
		```
		Old:
		from game_skeleton import pause_menu
		from game_skeleton import game_bar
		
		New:
		import pause_menu
		import game_bar
		```
	  This is due to differences in python versions.

### Installing dependencies
##### Arch Linux
	```
	pacman -S python # For the lastest version of python
	pacman -S python2-pygame
	```
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
	- First your game directory into 16-Bit-Hero-Arcade
	- Add game directory name to all file locations Ex
	
		```
		Old
		'resources/music/song.wav'
		New
		'cups/resources/music/song.wav'
		```
	- Add entry to menu.py and arcade.py
	- Import the screen from our arcade.py through the argument parameters for your game Ex. def __init__(self, screen)
	- Have your game inheret from game skeleton
		
		```
		class Cups(game_skeleton.Game_Skeleton)
		```
		
	- Add in necessary code for implementing the game skeleton (contains an game bar and pause menu)
		
		```
		# load music and sounds
		self.__screen = screen
		self.__game_skeleton = game_skeleton.Game_Skeleton(self.__screen)
		self.__screen.get_rect().height = self.__game_skeleton.get_game_height()
		
		# Inside game loop
		# Score is not necessary
		self.__game_skeleton.blit_game_bar(self.__game_title, self.__game_score)
		
		# Inside event handler
		pause options = self.__game_skeleton.events(event)
		if pause_options == 0:
			self.__running = False
			return True
		elif pause_options == 1:
			self.__running = False
		```
	- The game skeleton demo (gs_demo) is a good example of a blank slate for a game
	- Enjoy the benefits of a game bar, pause menu, and resolution!
	
	
	###### Workflow
1. Clone your fork to local computer:

	```
	git clone git@github.com:NAME/Ladon-Games.git
	```
2. Add the master branch as the upstream

	```
	git remote add upstream git@github.com:JormungandrGames/Ladon-Games.git
	```
3. Create a branch with this format

	```
	git branch update_type/feature_issue
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
		git clone git@github.com:NAME/Ladon-Games.git
		cd Ladon-Games

		git checkout -b issue_# master
		git pull https://github.com/NAME/16-Bit-Hero-Arcade.git issue_#

		fix conflicts

		git add .
		git commit -m "Message"

		git checkout master
		git merge --no-ff issue_#
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
	git branch -d issue_#
	```

