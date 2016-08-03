from . import FORBIDDEN, KING, QUEEN, BISHOP, ROOK, KNIGHT, FREE


class Board:
    def __init__(self, len_x, len_y):
        self.len_x = len_x
        self.len_y = len_y
        self.board = []
        self.combinations = set([])
        self.reset()

    def reset(self):
        """
        Reset board to initial state
        """
        self.board = [0] * self.len_x * self.len_y

    def sign_indexes(self, indexes=[], cell_type=FORBIDDEN):
        """
        To check position availabilities for chess pieces should be signed
        once then data will be used all others for the current trial.
        :param indexes: list of indexes ranges between 0 with given number of rows multiplication.
        :param cell_type: FORBIDDEN, CRITICAL
        """
        for index in indexes:
            if self.board[index] != FREE:
                return False
            self.board[index] = cell_type
        return True

    def print_board(self):
        """
        Human readable print of board.
        """
        printed_board = ""
        for x in range(self.len_x * self.len_y):
            if x % self.len_x == 0:
                printed_board += "\n"
            value = self.board[x]
            if value in [KING, QUEEN, BISHOP, ROOK, KNIGHT]:
                printed_board += "{} ".format(value)
            elif value == FORBIDDEN:
                printed_board += "X "
            else:
                printed_board += "{} ".format('.')
        print printed_board

    def place_it(self, piece):
        pass

    def place_them_all(self, *pieces):
        first_piece, rest_pieces = pieces[0], pieces[1:]
