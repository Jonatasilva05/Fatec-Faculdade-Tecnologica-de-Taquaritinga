   <img src="https://i.pinimg.com/originals/f7/b7/5e/f7b75eb944d396a563820ecdc002eb74.gif"
    style="center"
     /> 

# Alien Invasion
- Alien Invasion project from book Python Crash Course by Eric Matthes

## Requirements and Running Notes
- installation of Python
- install Pygame library if not already installed (from command line: pip install pygame)
- clone this repository: [https://github.com/RyvynYoung/alien_invasion](https://github.com/RyvynYoung/alien_invasion)
- open and run the alien_invasion.py file (the other files in the repo are needed for this file to run)
- this will open a new window with the game
    - FYI - this is slow to load for me, you may need to give it 30 seconds to fully load before clicking Play button

## Game Synopsis
In Alien Invasion, the player controls a rocket ship that appears at the bottom center of the screen. The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. The player shoots and destroys the aliens. If the player shoots all of the aliens, a new fleet appears that moves faster than the previous fleet. If any alien hits the player's ship or reaches the bottom of the screen. the player loses a ship. If the player loses three ships, the game ends.

**My Customizations:** tracking all time highest score, finding way to use relative path in VScode so that others can clone repo

**Learning Takeaways:** making and using Classes, refactoring and helper methods, Pygame library, larger project using multiple files, Visual Studio, write to and read from files

**Debug solutions:**
- File not found error, use full path for file
- remember to READ the error messages! They tell you where the problem is!
- Full path will not work for production (others won't have same file path)
    - code added to get current working directory and add to file path to enable reading from and writing to text file
