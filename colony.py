import random as rn
import numpy as np
from numpy.random import choice as np_choice

#Creates AntColony class
class AntColony(object):
    #Creates initial values
    def __init__(self, board, n_ants, decay, alpha=1, beta=1):

        self.board = board
        self.n_ants = n_ants
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    #Runs Ant Algorithm
    def run(self):
        shortest_path = 0
	shortest_path_board;
        for i in range(self.n_ants):
	    gen_ant()
            path = path_dist
            if shortest_path < path:
                shortest_path = path		
            self.update_pheronome()

        print(shortest_path_board));     
        return shortest_path

    #Updates pheromone value
    def update_pheronome(self, path):        
        for node in path:
	        node.phero *= self.decay
                node.phero += ...

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
        
        
