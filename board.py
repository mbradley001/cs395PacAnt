#Creates Node class
class Node:
  #Creates and gives initial values 
  def __init__(self, phero, ch, x, y):
    self.phero = phero
    self.c = ch
    self.x = x
    self.y = y
    #TODO overload comparison operators to compare phero

#Creates board
class Board:
#gets initial board values
  def __init__(self, p):
    
    self.b = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X      XX              G X",
    "X X    XX           XXXX X",
    "X      XX       P   XXXX X",
    "X      XX  XXX      XXXX X",
    "X      XX    X  XX       X",
    "X XXX  XX    X   X X     X",
    "X   X        X   X    X  X",
    "X   XX XXXX           X  X",
    "X            XXXX X   X  X",
    "X    X    XXXXXXX    XXXGX",
    "X X  X                 X X",
    "X X XXX  XXXXX  X  XXX X X",
    "XG    O         X    X   X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXX"]
    self.startP = p
    self.rows, self.cols = len(self.b[0]), len(self.b)
    self.arr = []
    self.parseBoard()
  
  #Parse through board
  def parseBoard(self):
    j = 0
    for line in self.b:
      i = 0
      xlist = []
      for ch in line:
        n = Node(self.startP, ch, j, i)
        xlist.append(n)
        i+=1
      self.arr.append(xlist)
      j+=1

  def print_path(self, path):
     nodes = self.arr
     for p in path:
        if nodes[p.x][p.y].c  != '$': 
           nodes[p.x][p.y].c = '*' 

     for line in nodes:
       for n in line:
         print(n.c, end=" ") 
       print()
     print("\n\n\n")


  #Find piecs in board(ANT, Ghost, POtato)
  def findPiece(self, c):
    foundList = []
    for xList in self.arr:
      for n in xList:
        if n.c == c:
          foundList.append(n)
    return foundList

  #resets the chars in each node back to start state
  def reset_chars(self):
     for c in range(self.rows):
        for r in range(self.cols):
           self.arr[r][c].c = self.b[r][c]

  #Prints the board
  def printBoard(self):
    for line in self.arr:
      for n in line:
        print(n.c, end=" ") 
      print()
    print("\n\n\n")
 

"""
def main():
#Board look so shiny
  b = [
    "XXXXXXXXXXXXXXXX",
    "XP     XX   G  X",
    "X XXXX XX XXXX X",
    "X XXXX XX XXXX X",
    "X XXXX XX XXXX X",
    "X      G       X",
    "X XXXXXXXXXXXX X",
    "X X          X X",
    "X X XXXXXXXX X X",
    "X   X      X   X",
    "XXX X XXXX X XXX",
    "XXX          XXX",
    "XXX X XXXX X XXX",
    "X   X      X   X",
    "X X XXXXXXXX X X",
    "X X      G   X X",
    "X XXXXXXXXXXXX X",
    "X      XX      X",
    "X XXXX XX XXXX X",
    "X XXXX XX XXXX X",
    "X XXXX XX XXXX X",
    "X  G   XX   O  X",
    "XXXXXXXXXXXXXXXX"]

  board = Board(b)
  board.parseBoard()
  board.printBoard()
  board.findPiece("G")

main()"""
