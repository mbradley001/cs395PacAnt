class Node:
  def __init__(self, phero, ch):
    self.phero = phero
    self.ch = ch

class Board:
  def __init__(self, boardL):
    self.b = boardL

  def printBoard(self):
    for line in self.b:
      for ch in line:
        print(ch, end='')
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
  board.printBoard()

main()
