from chess_piece import chessPiece

class Rook(chessPiece):
    SYMBOL = "R"

    def __init__(self, board, board_position):
        super().__init__(board, board_position, self.SYMBOL)

    def step(self, new_board_position):
        dx, dy = self.getMoveDelta(new_board_position)
        if not ((dx == 0 and dy != 0) or (dx != 0 and dy == 0)):
            raise Exception(f"{new_board_position} is an illegal move for rook at {self.getCurPosition()}.")
        self.make_move(new_board_position)
