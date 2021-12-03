# PacmanPython

Yet another remix of my Pac-Man game made in Python. Hopefully this one will be the last one but we shall see. 

What's staying the same:
  - Pygame will still be used, as I honestly don't really want to lwarn yet another game engine
  - While I'm grabbing new image files for them anyway, pacman and the ghosts will be mostly untouched. Hopefully

Rather than making walls and pellets, and thus needing the ghosts to effectively bounce off of them, this time I'm shooting for a tile based approach. This should help the ghosts "see" where they are and "see" ahead of themselves and be able to do some routing. Should hopefully make the AI easier to setup. But we shall see

TODO:
  - Make the map. Yet again
  - Add Pac-Man and the ghosts into the new map
  - Make sure Pac-Man collisions works with the walls and with the pellets
  - Insert all the ghosts, using the random movement as done originally
  - Create the AI logic for the ghosts
  - Implement the usual game stuff (Score, HighScore, Lives)
  - Implement the menu (Should be just copy and paste over)

BONUSES (For now)
  - Implement Power Pellet and functionality
  - Add states to ghosts
  - Death animation
  - Interlude animation
