import unittest
from domain.board import Board
from domain.Cell import Cell, ValidCell

class TestBoard(unittest.TestCase):
    def test_board(self):
        board = '[[0, 0, 0, 0, 0]]'
        self.board=Board(1,5)
        self.board.create_board()
        self.assertEqual(board, str(self.board.get_board()))

        self.board = Board(6,6)
        self.board.create_board()
        moves=self.board.available_moves()
        self.assertEqual(len(moves), 36)

        self.assertEqual(self.board.get_rows(), 6)
        self.assertEqual(self.board.get_columns(), 6)

        self.board.set_row(5)
        self.board.create_board()
        moves = self.board.available_moves()
        self.assertEqual(len(moves), 30)

        self.board.set_column(5)
        self.board.create_board()
        moves = self.board.available_moves()
        self.assertEqual(len(moves), 25)


