class Node:
  def __init__(self, phero, ch, x, y):
    self.phero = phero
    self.c = ch
    self.x = x
    self.y = y

class Board:
  def __init__(self, boardL):
    self.b = boardL
    rows, cols = (23,16)
    self.arr = []

  def parseBoard(self):
    j = 0
    for line in self.b:
      i = 0
      xlist = []
      for ch in line:
        n = Node(0, ch, i, j)
        xlist.append(n)
        i+=1
      self.arr.append(xlist)
      j+=1

  def findPiece(self, c):
    foundList = []
    for xList in self.arr:
      for n in xList:
        if n.c == c:
          foundList.append(n)
    for n in foundList:
      print("Piece: " + n.c + "\nFound at: (" + str(n.x) + ", " + str(n.y) + ")\n")
    return foundList

  def printBoard(self):
    for line in self.arr:
      for n in line:
        print(n.c, end='')
      print()

def main():
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

main()
