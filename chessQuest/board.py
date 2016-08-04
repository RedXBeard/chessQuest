from . import FORBIDDEN, KING, QUEEN, BISHOP, ROOK, KNIGHT, FREE, PIECES


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
            if self.board[index] in [QUEEN, KING, ROOK, BISHOP, KNIGHT]:
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
        print "Total combination count: {}".format(len(self.combinations))

    def place_them_all(self, pieces):
        """
        Entry point of recursion to find all possible position of given pieces.
        :param pieces: List of given chess pieces.
        """
        first_piece, rest_pieces = pieces[0], pieces[1:]
        for index in range(len(self.board)):
            self.reset()
            self.board[index] = first_piece
            self.place_them(["{}_{}".format(first_piece, index)], rest_pieces)

    def place_them(self, combination=[], pieces=[]):
        """
        Found all suitable positions for each pieces.
        :param combination: list of string of piece and index of position which is found as suitable.
        :param pieces: by the recursion list of given chess pieces.
        """
        if not pieces:
            self.combinations.add(','.join(sorted(combination)))
            return

        first_piece, rest_pieces = pieces[0], pieces[1:]

        self.reset()
        place_them = map(lambda x: x.split('_'), combination)
        for piece, piece_index in place_them:
            self.board[int(piece_index)] = piece
            for func in PIECES[piece]['movements']:
                func(self, int(piece_index))

        for index in self.free_cells():
            result = True
            for func in PIECES[first_piece]['movements']:
                result = result and func(self, int(index))
            if result:
                self.place_them(
                    combination=combination + ["{}_{}".format(first_piece, index)], pieces=rest_pieces)
