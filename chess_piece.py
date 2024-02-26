class chessPiece:

  SYMBOL = "*"

  def __letterToNum(letter):
    return ord(letter.lower())-96

  def __numToLetter(num:int):
    return chr(num + 96)

  def posToXY(self, boardStr):
    """
    Return x, y coordinates to letter number chess piece position, e.g.: 'b6' -> 2,6
    """
    return (__class__.__letterToNum(boardStr[0]),int(boardStr[1]))
  
  def XYToPos(self, x:int, y:int):
    """
    Return human friendly chess piece position for x, y coordinates, e.g.: 3,2 -> 'c2'
    """
    return(f'{__class__.__numToLetter(x)}{str(y)}')

  def __init__(self, board, board_position, symbol):
    self.board = board
    self.x, self.y = self.posToXY(board_position)
    self.symbol = symbol
    board.set(self.x, self.y, self.symbol)

  def position_free(self, x,y):
      '''
      Checks if position is ocupied or free
      
      Arguments
      ---------
      x : int
          column number position on board (start from 1)
      y : int
          raw number position on board (start from 1)
          
      Returns:
          bool : True if position is free, False if position is occupied
      '''
      return self.board.get( x, y) == self.board.EMPTY_FIELD
  
  def position_in_bounds(self, x, y):
      return (1 <= x <= 8) and (1 <= y <= 8)

  def getCurPosition(self):
    return self.XYToPos(self.x, self.y)

  def checkStep(self, new_board_position):
    new_x, new_y = self.posToXY(new_board_position)
    if not self.position_in_bounds(new_x, new_y):
      raise Exception(f"Position {new_board_position} is not on the board")
    elif not self.position_free(new_x, new_y):
      raise Exception(f"Position {new_board_position} is already ocupied by {self.board.get(new_x, new_y)}")
    else:
      print("New position in bounds.")

  def make_move(self, new_board_position):
      self.checkStep(new_board_position)
      new_x, new_y = self.posToXY(new_board_position)
      self.board.set(self.x, self.y, self.board.EMPTY_FIELD)
      self.x = new_x
      self.y = new_y
      self.board.set(self.x, self.y, self.symbol)

  def getMoveDelta(self,new_board_position):
    new_x, new_y = self.posToXY(new_board_position)
    return (new_x - self.x, new_y-self.y)