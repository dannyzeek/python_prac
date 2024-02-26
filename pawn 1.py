from chess_piece import chessPiece

class Pawn(chessPiece):
    SYMBOL = "p"

    def __init__(self, board, board_postion):
        super().__init__(board, board_postion, self.SYMBOL)

    def step(self, new_board_position):
        dx, dy = self.getMoveDelta(new_board_position)
        if not (dx == 0 and (dy == 1 or ( self.y ==2 and dy == 2))):
            raise Exception(f"{new_board_position} is Illegal move for pawn at {self.getCurPosition()}.")
        self.make_move(new_board_position)