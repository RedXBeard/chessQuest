from datetime import datetime

from chessQuest.utils import cached
from . import FORBIDDEN, KING, QUEEN, BISHOP, ROOK, KNIGHT, FREE, PIECES


class Board:
    def __init__(self, len_x, len_y):
        self.len_x = len_x
        self.len_y = len_y
        self.board = []
        self.combinations = set([])
        self.reset()
        self.spend = 0

    @property
    def spend_time(self):
        return str(self.spend)

    def reset(self):
        """
        Reset board to initial state
        """
        self.board = [FREE] * self.len_x * self.len_y

    def sign_indexes(self, indexes=[], cell_type=FORBIDDEN):
        """
        To check position availabilities for chess pieces should be signed
        once then data will be used all others for the current trial.
        :param indexes: list of indexes ranges between 0 with given number of rows multiplication.
        :param cell_type: FORBIDDEN, CRITICAL
        """
        for index in indexes:
            if self.board[index] in [QUEEN, KING, ROOK, BISHOP, KNIGHT]:
                return False
            self.board[index] = cell_type
        return True

    @cached
    def piece_movements(self, piece, pointed_index):
        """
        Working with collection of movement methods of each piece,
        grouping them all and returns it.
        By the cached decorator help, indexes do not collected with movements.
        :param piece: one of king, queen, rook, knight, bishop.
        :param pointed_index: index of board which was tried to the piece.
        :return: list of movable indexes of the piece.
        """
        indexes = []
        for func in PIECES[piece]['movements']:
            indexes.extend(func(self, pointed_index))
        return indexes

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
        print(printed_board)

    def free_cells(self):
        """
        Find all indexes that are free yet on board.
        :return: Free cell indexes of board as list
        """
        cells = []
        for index in range(len(self.board)):
            if self.board[index] == FREE:
                cells.append(index)
        return cells

    def show_combinations(self, limit=10):
        """
        Give information about board preparation for given chess pieces
        sample set is displaying and total count will be informed.
        :param limit: not all combinations but first 10 to show.
        :return: prints total count and display sample of combinations.
        """
        for combination in list(self.combinations)[:limit]:
            combination = map(lambda x: x.split('_'), combination.split(','))
            self.reset()
            for piece, index in combination:
                self.board[int(index)] = piece
            self.print_board()
        print("Total combination count: {}".format(len(self.combinations)))

    def place_them_all(self, pieces):
        """
        Entry point of recursion to find all possible position of given pieces.
        :param pieces: List of given chess pieces.
        """
        t1 = datetime.now()
        first_piece, rest_pieces = pieces[0], pieces[1:]
        for index in range(len(self.board)):
            self.reset()
            self.board[index] = first_piece
            self.place_them(["{}_{}".format(first_piece, index)], rest_pieces, len(pieces))
        self.spend = datetime.now() - t1

    def place_them(self, combination=[], pieces=[], total_count=0):
        """
        Found all suitable positions for each pieces.
        :param combination: list of string of piece and index of position which is found as suitable.
        :param pieces: by the recursion list of given chess pieces.
        :param total_count: total number of pieces at the beginning
        """
        if not pieces and len(combination) == total_count:
            self.combinations.add(','.join(sorted(combination)))
            return

        first_piece, rest_pieces = pieces[0], pieces[1:]

        self.reset()
        place_them = map(lambda x: x.split('_'), combination)
        for piece, piece_index in place_them:
            indexes = self.piece_movements(piece, int(piece_index))
            self.sign_indexes(indexes)
            self.board[int(piece_index)] = piece

        for index in self.free_cells():
            indexes = self.piece_movements(first_piece, index)
            result = self.sign_indexes(indexes)
            if result:
                self.place_them(
                    combination=combination + ["{}_{}".format(first_piece, index)],
                    pieces=rest_pieces, total_count=total_count)
