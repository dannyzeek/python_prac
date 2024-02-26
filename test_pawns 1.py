from board import Board
from pawn import Pawn

my_board=Board()

my_Pawns=[Pawn(my_board,'a2'), Pawn(my_board,'b2'), Pawn(my_board,'c2'), Pawn(my_board,'d2')]
black_pawn = Pawn(my_board,'b7')

my_board.print()
# my_Pawns[0].step('a1')
# my_board.print()

for n in range(4,10):
  my_Pawns[1].step(f'b{n}')
  my_board.print()