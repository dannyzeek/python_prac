class Board:

#   EMPTY_FIELD = "·"
  EMPTY_FIELD = "░"

  def __init__(self):
    """
    Initilize board and fill it with `empty cells`
    """
    self.board = [self.EMPTY_FIELD for _ in range(64)]

  def pos(self,x, y):
      """
      Calculate 2D position on chess board stored in flat array
      Start counting from index 1
      
      Arguments
      ---------
      x : int
          column number position on board (start from 1)
      y : int
          raw number position on board (start from 1)
      """
      return (y - 1) * 8 + (x - 1)

  def set(self, x, y, symbol):
      """
      Set symbol to chess board in x, y coordinated
      
      Arguments
      ---------
      board : list(str)
          Chess board flat representation
      x : int
          column number position on board (start from 1)
      y : int
          raw number position on board (start from 1)
      symbol: str
          string to setup by coordinates
      """
      self.board[self.pos(x,y)] = symbol

  def get(self, x, y):
      return self.board[self.pos(x,y)]

  def print(self):
      print(" ", end = "|")
      for x in range(1,9):
          print (x, end = " ")
      print()
      print(" ", end = "|")
      for x in range(1,9):
          print ("_", end = " ")
      print()
      for y in reversed(range(1,9)):
          print(y, end = "|")
          for x in range(1,9):
              symbol = self.get( x, y)
              print (symbol, end = " ")
          print()

  def print_xl(self): 
    for y in reversed(range(1,9)):
        print("{:─^36}".format(""),end="\n")
        print("{:^3}║".format(y),end="")
        for x in range(1,9):
            symbol = self.get( x, y)
            print("{:░^3}|".format(symbol),end="")
        print()
    print("{:─^36}".format(""),end="\n")
    for x in range(0,9):
        print("{:^3}│".format(x if x > 0 else '*'),end="")
    print()