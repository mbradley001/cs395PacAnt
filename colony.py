import random as ran
from board import Node, Board


#Creates AntColony class
class AntColony(object):
    #Creates initial values
    def __init__(self, board, n_ants, decay, alpha=1, beta=1):

        self.board = board
        self.n_ants = n_ants
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def decayBoard(self):
        for xList in self.board.arr:
            for n in xList:
                n.phero = n.phero * self.decay

    def unleash_the_ants(self):
        
        shortest_path = set()
        for i in range(self.n_ants):
            path = self.gen_path()
           
            if self.path_dist(shortest_path) >= self.path_dist(path) and self.path_dist(path) != 0:
                shortest_path = path

            self.decayBoard()
            self.update_pheronome(path)
            if i%10 == 0:
              self.board.printBoard()
            self.board.reset_chars()
            path.clear() 

        return shortest_path


    def update_pheronome(self, path):        
        for node in path:
            if(self.path_dist(path) > 0):
               node.phero += 1/self.path_dist(path)
            else:
               pass

    def path_dist(self, path):
        return len(path)


    def gen_path(self):
#print("Gen path\n")
        path = set()
        pac = self.board.findPiece('P')[0]#start node for pac

        while(True):
            move = self.pick_pac_move(pac)
#print(str(move) + " <-move")
            if(move.x == pac.x and move.y == pac.y):
               path.clear()
               return path

            atTarget = self.movePiece(pac, move)

            path.add(move)
            pac = move

            if(atTarget):
               break

            atePac = self.moveGhosts(pac)
            if(atePac):
               break

        return path


    def pick_pac_move(self, p):
       moves = self.find_moves(p)

#print("PMove X", p.x,"Pmove Y", p.y)
#      print("Move X", moves[0].x,"move Y", moves[0].y)
#print("Move X", moves[1].x,"move Y", moves[1].y)
       for m in moves:
# print(m.c == 'G' or m.c == '*')
           if(m.c == 'G'):# or m.c == '*' or m.c == 'P'):
               moves.remove(m)

       if(len(moves) ==0):
           return p

       if(len(moves) == 1):
           return moves[0]

       total = 0
       for m in moves:
            total += m.phero

       sorted(moves, key=lambda x: x.phero)
       num = ran.random()
       i = 0
       for e in moves:
#         print("num: " + str(num))
#         print("i" , i)
          if(num > i and num <= (e.phero/total)+i):
              return e
          else:
              i += e.phero/total

    def moveGhosts(self, pac):
       ghosts = self.board.findPiece('G')
       
       for g in ghosts:
#print("ghost(",g.x,",",g.y,")")
           move = self.pick_ghost_move(g, pac)
           if (self.movePiece(g, move)):
               return True
          

    def movePiece(self, n1, n2):
#        print(type(n1))
         if(n1.c == 'G'):
            if(n2.c == 'P'):
               self.board.arr[n1.x][n1.y].c = '.'
               self.board.arr[n2.x][n2.y].c = '@'
               return True
            elif(n2.c == 'G'):
               pass
            else:
               self.board.arr[n1.x][n1.y].c = '.'
               self.board.arr[n2.x][n2.y].c = 'G'

         elif(n1.c == 'P'):
            if(n2.c == 'O'):
               self.board.arr[n1.x][n1.y].c = '*'
               self.board.arr[n2.x][n2.y].c = '$'
               return True  
            else:
               self.board.arr[n1.x][n1.y].c = '*'
               self.board.arr[n2.x][n2.y].c = 'P'
         return False


    #chooses ideal ghost move for seeking behavior
    def pick_ghost_move(self, ghost, p):
       moves = self.find_moves(ghost)
       for m in moves:
          if(m.c == 'O'):
             moves.remove(m)

       if(len(moves) == 0):
          return ghost
       
       choice = moves[0]

       for m in moves:
          man = self.manhattan(m, p)
          if(man <= self.manhattan(choice, p)):
             choice = m

       return choice 


    #returns path length
    def path_dist(self, path):
        return len(path)

    def manhattan(self, g, pac):
         return (abs(pac.x - g.x) + abs(pac.y - g.y)) 

    #finds non-wall moves given a node
    def find_moves(self, n):

       moves = []
#      print("b.x", self.board.rows, "b.y", self.board.cols)
#      print("n.x:",n.x, "n.y",n.y)
       if((n.y - 1) >= 0):
          if(self.board.arr[n.x][n.y-1].c != 'X'):           
             moves.append(self.board.arr[n.x][n.y-1])

       if((n.x - 1) >= 0):
          if(self.board.arr[n.x-1][n.y].c != 'X'):           
             moves.append(self.board.arr[n.x-1][n.y])

       if((n.x + 1) < self.board.cols):
          if(self.board.arr[n.x+1][n.y].c != 'X'):           
             moves.append(self.board.arr[n.x+1][n.y])

       if((n.y + 1) < self.board.rows):
          if(self.board.arr[n.x][n.y+1].c != 'X'):           
             moves.append(self.board.arr[n.x][n.y+1])
#      print("Number of moves found", len(moves), "\n")
       return moves

board = Board()
ant = AntColony(board, 100, .75)
print ("Path length: ", len(ant.unleash_the_ants()))

