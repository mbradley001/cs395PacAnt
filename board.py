class Node:
  def __init__(self, phero, ch):
    self.phero = phero
    self.c = ch

class Board:
  def __init__(self, boardL):
    self.b = boardL
    rows, cols = (23,16)
    self.arr = []

  def parseBoard(self):
    for line in self.b:
      xlist = []
      for ch in line:
        n = Node(0, ch)
        xlist.append(n)
      self.arr.append(xlist)

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

main()
