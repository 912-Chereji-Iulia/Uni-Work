from domain.Cell import Cell

class Board:
    def __init__(self, row=0, column=0):
        self._row = row
        self._column = column
        self._board = []

    def get_board(self):
        return self._board

    def get_rows(self):
        return self._row

    def set_row(self, row):
        self._row = row

    def get_columns(self):
        return self._column

    def set_column(self, col):
        self._column = col

    def available_moves(self):
        """
        :return: a list of available positions for the moves
        """
        available = []
        for i in range(self.get_rows()):
            for j in range(self.get_columns()):
                if self._board[i][j] == 0:
                    available.append(Cell(i, j))
        return available

    def create_board(self):
        """
        This function creates the board with the given dimensions.
        The board will be a list of lists, each list will represent a row, and each element of these lists will
        represent a column.
        """
        for r in range(self._row):
            lst = []
            for c in range(self._column):
                lst.append(0)
            self._board.append(lst)

    def __str__(self):
        string = "\n   "
        for x in range(self._column):
            string += str(x) + '   '
        for x in range(self._row):
            string += "\n " + "-" * (4 * self._column + 1) + "\n" + str(x) + '|'
            for y in range(self._column):
                if self._board[x][y] == 1:
                    string += ' \033[35m0\033[0m |'
                elif self._board[x][y] == 2:
                    string += ' \033[93mX\033[0m |'
                elif self._board[x][y] == -1:
                    string += '---|'
                else:
                    string += '   |'
        string += "\n "+"-" * (4 * self._column + 1) + "\n"
        return string

    def reset_board(self):
        self._row = 0
        self._column = 0
        self._board = []

    def __len__(self):
        return len(self._board)
