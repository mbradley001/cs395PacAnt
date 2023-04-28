import random as rn
import numpy as np
from numpy.random import choice as np_choice

class AntColony(object):

    def __init__(self, board, n_ants, decay, alpha=1, beta=1):

        self.board = board
        self.n_ants = n_ants
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        shortest_path = 0
	shortest_path_board;
        for i in range(self.n_ants):
	    gen_path()
            path = path_dist
            if shortest_path < path:
                shortest_path = path
                shortest_board = self.b     
            self.update_pheronome()

        print(shortest_path_board));     
        return shortest_path

    def update_pheronome(self, path):        
        for node in path:
	        node.phero *= self.decay
                node.phero += ...

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

