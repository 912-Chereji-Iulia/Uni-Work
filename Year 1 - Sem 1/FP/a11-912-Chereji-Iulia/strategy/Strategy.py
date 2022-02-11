import random
from domain.Cell import Cell
from domain.Cell import ValidCell
from domain.board import Board


class Strategy:
    def __init__(self, board:Board):
        self._board = board
        self._valid = ValidCell()
        self._start_odd = False

    def get_board(self):
        return self._board

    def set_row(self, row):
        self._board.set_row(row)

    def set_column(self, column):
        self._board.set_column(column)

    def create_board(self):
        self._board.create_board()
        self._start_odd = False

    def boarding(self, point):
        """
        boards the neighborhood of a given point
        :param point:
        :return:
        """
        x = point.get_row()
        y = point.get_column()
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i < self._board.get_rows() and i >= 0 and j < self._board.get_columns() and j >= 0:
                    if self._board.get_board()[i][j] == 0:
                        self._board.get_board()[i][j] = -1

    def apply_strategy(self, row, column, moves, x, y):
        if len(moves) == row * column: #if the computer is the first one to move on an odd board
            centre_x = int(row // 2)
            centre_y = int(column // 2)
            self._board.get_board()[centre_x][centre_y] = 2
            pos = Cell(centre_x, centre_y)
            self.boarding(pos)
            self._start_odd = True
            return pos

        if len(moves) != row * column: #if it's not the first move, we use the mirrored position
            pos = self.get_mirror_position(int(x), int(y))
            self._board.get_board()[int(pos.get_row())][int(pos.get_column())] = 2
            self.boarding(pos)
            return pos

    def get_mirror_position(self, x, y):
        """
        gets the mirrored position of a given position
        :param x:
        :param y:
        :return:
        """
        row = self._board.get_rows()-1
        col = self._board.get_columns()-1
        if self._board.get_board()[x][col - y] == 0:
            return Cell(x, col - y)
        if self._board.get_board()[row - x][y] == 0:
            return Cell(row - x, y)
        if self._board.get_board()[row - x][col - y] == 0:
            return Cell(row - x, col - y)

    def decide_move(self, computer, row, column, moves):
        """
        return 1 if the strategy can be applied or 2 if it has to move randomly
        """
        if computer is True and len(moves) == row * column:
            if row % 2 == 1 and column % 2 == 1:
                return 1
        if self._start_odd is True and len(moves) != row * column:
            return 1
        return 2

    def random_move(self, positions):
        """
        random move for the computer
        :param positions:
        :return:
        """
        i = random.randint(0, len(positions) - 1)
        self._board.get_board()[positions[i].get_row()][positions[i].get_column()] = 2
        self.boarding(positions[i])
        return positions[i]

    def computer_move(self, computer, x, y):
        """
        computers move
        """
        av_moves = self._board.available_moves()
        rows = self._board.get_rows()
        columns = self._board.get_columns()
        next_move = self.decide_move(computer, rows, columns, av_moves)
        if next_move == 1:
            return self.apply_strategy(rows, columns, av_moves, x, y)
        elif next_move == 2:
            return self.random_move(av_moves)

    def player_move(self, x, y):
        """
        makes the players move
        :param x: x coordinate
        :param y: y coordinate
        :return:
        """
        self._valid.valid_cell(x, y, self._board)
        point = Cell(x, y)
        self._board.get_board()[int(x)][int(y)] = 1
        self.boarding(point)

    def game_not_over(self):
        '''
        :return: true if there are available moves
        '''
        if self._board.available_moves():
            return True
        return False

    def reset_board(self):
        """
        resets the board to the initial form
        :return:
        """
        self._board.reset_board()