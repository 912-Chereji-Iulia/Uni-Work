class Cell:
    def __init__(self, row, col):
        self._row = int(row)
        self._column = int(col)

    def get_row(self):
        return self._row

    def get_column(self):
        return self._column

class ValidCell:
    @staticmethod
    def valid_cell(x, y, board):
        if not isinstance(x,int) or not isinstance(y,int):
            raise Exception("The coordinates should be integers")
        if board.get_board()[x][y] in [-1, 1, 2]:
            raise Exception("Square is already taken!")
        if y < 0 or x < 0 or y >= board.get_columns() or x >= board.get_rows():
            raise Exception("The coordinates are out of the board!")