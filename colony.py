import random as rn
import numpy as np
from numpy.random import choice as np_choice

<<<<<<< HEAD
class AntColony(object):

=======
#Creates AntColony class
class AntColony(object):
    #Creates initial values
>>>>>>> 5e00fda085022e48283babfc9c4584fc002b8a16
    def __init__(self, board, n_ants, decay, alpha=1, beta=1):

        self.board = board
        self.n_ants = n_ants
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

<<<<<<< HEAD
=======
    #Runs Ant Algorithm
>>>>>>> 5e00fda085022e48283babfc9c4584fc002b8a16
    def run(self):
        shortest_path = 0
	shortest_path_board;
        for i in range(self.n_ants):
<<<<<<< HEAD
	    gen_path()
            path = path_dist
            if shortest_path < path:
                shortest_path = path
                shortest_board = self.b     
=======
	    gen_ant()
            path = path_dist
            if shortest_path < path:
                shortest_path = path		
>>>>>>> 5e00fda085022e48283babfc9c4584fc002b8a16
            self.update_pheronome()

        print(shortest_path_board));     
        return shortest_path

<<<<<<< HEAD
=======
    #Updates pheromone value
>>>>>>> 5e00fda085022e48283babfc9c4584fc002b8a16
    def update_pheronome(self, path):        
        for node in path:
	        node.phero *= self.decay
                node.phero += ...

<<<<<<< HEAD
    def path_dist(self, path):
        return len(path)

    def gen_path(self, start):
        path = []
        visited = []
        pac = self.board.findPiece('P')
        visited.append(pac)
        while(True):
            move = self.pick_move(pac)
	    atTarget = self.movePiece(pac, move)

            path.append(move)
            visited.append(move)
	    pac = move

            if(atTarget):
	      break

            atePac = self.moveGhosts(pac)
            if(atePac):
	      break

        return path


    def pick_move(self, visited):
       ...


    def find_moves(self):
       ...

       
    def moveGhosts(self, pac):
       ghosts = self.board.findPiece('G')
       for g in ghosts:
           move = pick_ghost_move(g)
	   movePiece(g, move)
           ...

    def movePiece(self, n1, n2):
        if(n1.c == 'G'):
	   self.arr[n1.x][n1.y].c = '.'
	   self.arr[n2.x][n2.y].c = 'G'
	 else if(n1.c == 'P'):
	   self.arr[n1.x][n1.y].c = '*'
	   self.arr[n2.x][n2.y].c = 'P'
 

    def pick_ghost_move(self, ghost):
       ...

=======
    #Gets path distance
    def path_dist(self, path):
        return len(path)

    #Generates Ant
    def gen_ant(self, start):
        path = []
        visited = []
        visited.append(start)
        prev = start
        for i in range(len(self.distances) - 1):
            move = self.(visited)
            path.append(move)
            prev = move
            visited.append(move)
        path.append((prev, start)) # going back to where we started    
        return path
    #Picks move based on phero value
    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0

        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)

        norm_row = row / row.sum()
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move

    def find_move(self):
        
        
>>>>>>> 5e00fda085022e48283babfc9c4584fc002b8a16
