Authors: Nathan Stettler, Camden Gilbert, Michael Bradley, and Joshua Mealy 
CMSC-395: Final Project
Date: 5/2/23

--Overview--
This program uses an ant algorithm to determine the optimal path to a target given a maze and obstacles with a seeking behavior.
The program uses ASCII characters to simulate the ant (Pac man) traversing the maze and the obstacles (ghosts) seeking Pac Man.

--Running--
python3 colony.py

--Parameters--
There are three parameters that can be changed: the number of ants, the decay rate, and alpha. These get passed into the AntColony
constructor in that order. The constructor is called at the bottom of colony.py if you wish to change them.

--The Board--
The start state of the board is in a list of strings in the board class's INIT. If you wish to change it in any way, make sure there is at least one ghost, an O, a P, and that
the board remains a rectangle.

--Disclaimer--
Due to the four dierctional movement of the objects in this simulation, it is possible to get in an infinte loop caused by a ghost pinning pacman
against a wall and them just moving up and down continuously. I does not happen often, but it is possible.
