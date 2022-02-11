import unittest

from domain.Cell import Cell
from domain.board import Board
from strategy.Strategy import Strategy


class TestAI(unittest.TestCase):
    def test_ai(self):
        b = Board(5, 5)
        self.board = Strategy(b)
        self.board.create_board()
        self.assertEqual(str(b), str(self.board.get_board()))
        self.assertEqual(self.board.reset_board(), None)
        self.assertFalse(self.board.game_not_over())

        self.board = Strategy(Board(3, 5))
        self.board.create_board()
        self.board.computer_move(True, 0, 0)
        self.assertTrue(self.board.game_not_over())
        self.board.player_move(1, 0)
        self.assertTrue(self.board.game_not_over())
        self.board.computer_move(True, 1, 0)
        self.assertFalse(self.board.game_not_over())

