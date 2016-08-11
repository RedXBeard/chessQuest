import unittest
from random import randrange, choice

from chessQuest import FREE, FORBIDDEN, PIECES_ORDER, KING, QUEEN, ROOK, BISHOP, KNIGHT
from chessQuest.board import Board


class ChessQuestTestCase(unittest.TestCase):
    def test_board_creation(self):
        board = Board(7, 7)
        self.assertEqual(len(board.board), 49)

    def test_reset_board(self):
        board = Board(7, 7)
        board.reset()
        self.assertEqual(len(filter(lambda x: x == FREE, board.board)), 49)

    def test_signing(self):
        board = Board(7, 7)
        indexes = set([])
        for i in range(1, randrange(49)):
            indexes.add(i and randrange(i) or 0)
        board.sign_indexes(indexes)
        self.assertEqual(len(filter(lambda x: x == FORBIDDEN, board.board)), len(indexes))

        # locate a piece
        board.reset()
        board.board[choice(list(indexes))] = 'K'
        self.assertFalse(board.sign_indexes(indexes))

    def test_freecells(self):
        board = Board(7, 7)
        self.assertEqual(49, len(board.free_cells()))
        indexes = set([])
        for i in range(randrange(49)):
            indexes.add(i and randrange(i) or 0)
        board.sign_indexes(indexes)
        self.assertEqual(set(board.free_cells()), set(range(0, 49)).difference(set(indexes)))

    def test_movement_king(self):
        board = Board(3, 3)
        board.board[0] = KING
        indexes = board.piece_movements(KING, 0)
        self.assertEqual(set([1, 3, 4]), set(indexes))

        board.reset()
        board.board[1] = KING
        indexes = board.piece_movements(KING, 1)
        self.assertEqual(set([0, 2, 3, 4, 5]), set(indexes))

        board.reset()
        board.board[2] = KING
        indexes = board.piece_movements(KING, 2)
        self.assertEqual(set([1, 4, 5]), set(indexes))
        board.reset()
        board.board[3] = KING
        indexes = board.piece_movements(KING, 3)
        self.assertEqual(set([0, 1, 4, 6, 7]), set(indexes))

        board.reset()
        board.board[4] = KING
        indexes = board.piece_movements(KING, 4)
        self.assertEqual(set([0, 1, 2, 3, 5, 6, 7, 8]), set(indexes))

        board.reset()
        board.board[5] = KING
        indexes = board.piece_movements(KING, 5)
        self.assertEqual(set([1, 2, 4, 7, 8]), set(indexes))

        board.reset()
        board.board[6] = KING
        indexes = board.piece_movements(KING, 6)
        self.assertEqual(set([3, 4, 7]), set(indexes))

        board.reset()
        board.board[7] = KING
        indexes = board.piece_movements(KING, 7)
        self.assertEqual(set([3, 4, 5, 6, 8]), set(indexes))

        board.reset()
        board.board[8] = KING
        indexes = board.piece_movements(KING, 8)
        self.assertEqual(set([4, 5, 7]), set(indexes))

    def test_movement_queen(self):
        board = Board(3, 3)
        board.board[0] = QUEEN
        indexes = board.piece_movements(QUEEN, 0)
        self.assertEqual(set([1, 2, 3, 4, 6, 8]), set(indexes))

        board.reset()
        board.board[1] = QUEEN
        indexes = board.piece_movements(QUEEN, 1)
        self.assertEqual(set([0, 2, 3, 4, 5, 7]), set(indexes))

        board.reset()
        board.board[2] = QUEEN
        indexes = board.piece_movements(QUEEN, 2)
        self.assertEqual(set([0, 1, 4, 5, 6, 8]), set(indexes))
        board.reset()
        board.board[3] = QUEEN
        indexes = board.piece_movements(QUEEN, 3)
        self.assertEqual(set([0, 1, 4, 5, 6, 7]), set(indexes))

        board.reset()
        board.board[4] = QUEEN
        indexes = board.piece_movements(QUEEN, 4)
        self.assertEqual(set([0, 1, 2, 3, 5, 6, 7, 8]), set(indexes))

        board.reset()
        board.board[5] = QUEEN
        indexes = board.piece_movements(QUEEN, 5)
        self.assertEqual(set([1, 2, 3, 4, 7, 8]), set(indexes))

        board.reset()
        board.board[6] = QUEEN
        indexes = board.piece_movements(QUEEN, 6)
        self.assertEqual(set([0, 2, 3, 4, 7, 8]), set(indexes))

        board.reset()
        board.board[7] = QUEEN
        indexes = board.piece_movements(QUEEN, 7)
        self.assertEqual(set([1, 3, 4, 5, 6, 8]), set(indexes))

        board.reset()
        board.board[8] = QUEEN
        indexes = board.piece_movements(QUEEN, 8)
        self.assertEqual(set([0, 2, 4, 5, 6, 7]), set(indexes))

    def test_movement_rook(self):
        board = Board(3, 3)
        board.board[0] = ROOK
        indexes = board.piece_movements(ROOK, 0)
        self.assertEqual(set([1, 2, 3, 6]), set(indexes))

        board.reset()
        board.board[1] = ROOK
        indexes = board.piece_movements(ROOK, 1)
        self.assertEqual(set([0, 2, 4, 7]), set(indexes))

        board.reset()
        board.board[2] = ROOK
        indexes = board.piece_movements(ROOK, 2)
        self.assertEqual(set([0, 1, 5, 8]), set(indexes))
        board.reset()
        board.board[3] = ROOK
        indexes = board.piece_movements(ROOK, 3)
        self.assertEqual(set([0, 4, 5, 6]), set(indexes))

        board.reset()
        board.board[4] = ROOK
        indexes = board.piece_movements(ROOK, 4)
        self.assertEqual(set([1, 3, 5, 7]), set(indexes))

        board.reset()
        board.board[5] = ROOK
        indexes = board.piece_movements(ROOK, 5)
        self.assertEqual(set([2, 3, 4, 8]), set(indexes))

        board.reset()
        board.board[6] = ROOK
        indexes = board.piece_movements(ROOK, 6)
        self.assertEqual(set([0, 3, 7, 8]), set(indexes))

        board.reset()
        board.board[7] = ROOK
        indexes = board.piece_movements(ROOK, 7)
        self.assertEqual(set([1, 4, 6, 8]), set(indexes))

        board.reset()
        board.board[8] = ROOK
        indexes = board.piece_movements(ROOK, 8)
        self.assertEqual(set([2, 5, 6, 7]), set(indexes))

    def test_movement_bishop(self):
        board = Board(3, 3)
        board.board[0] = BISHOP
        indexes = board.piece_movements(BISHOP, 0)
        self.assertEqual(set([4, 8]), set(indexes))

        board.reset()
        board.board[1] = BISHOP
        indexes = board.piece_movements(BISHOP, 1)
        self.assertEqual(set([3, 5]), set(indexes))

        board.reset()
        board.board[2] = BISHOP
        indexes = board.piece_movements(BISHOP, 2)
        self.assertEqual(set([4, 6, 8]), set(indexes))
        board.reset()
        board.board[3] = BISHOP
        indexes = board.piece_movements(BISHOP, 3)
        self.assertEqual(set([1, 7]), set(indexes))

        board.reset()
        board.board[4] = BISHOP
        indexes = board.piece_movements(BISHOP, 4)
        self.assertEqual(set([0, 2, 6, 8]), set(indexes))

        board.reset()
        board.board[5] = BISHOP
        indexes = board.piece_movements(BISHOP, 5)
        self.assertEqual(set([1, 7]), set(indexes))

        board.reset()
        board.board[6] = BISHOP
        indexes = board.piece_movements(BISHOP, 6)
        self.assertEqual(set([0, 2, 4]), set(indexes))

        board.reset()
        board.board[7] = BISHOP
        indexes = board.piece_movements(BISHOP, 7)
        self.assertEqual(set([3, 5]), set(indexes))

        board.reset()
        board.board[8] = BISHOP
        indexes = board.piece_movements(BISHOP, 8)
        self.assertEqual(set([0, 4]), set(indexes))

    def test_movement_knight(self):
        board = Board(3, 3)
        board.board[0] = KNIGHT
        indexes = board.piece_movements(KNIGHT, 0)
        self.assertEqual(set([5, 7]), set(indexes))

        board.reset()
        board.board[1] = KNIGHT
        indexes = board.piece_movements(KNIGHT, 1)
        self.assertEqual(set([8, 6]), set(indexes))

        board.reset()
        board.board[2] = KNIGHT
        indexes = board.piece_movements(KNIGHT, 2)
        self.assertEqual(set([3, 7]), set(indexes))
        board.reset()
        board.board[3] = KNIGHT
        indexes = board.piece_movements(KNIGHT, 3)
        self.assertEqual(set([8, 2]), set(indexes))

        board.reset()
        board.board[4] = KNIGHT
        indexes = board.piece_movements(KNIGHT, 4)
        self.assertEqual(set([]), set(indexes))

        board.reset()
        board.board[5] = KNIGHT
        indexes = board.piece_movements(KNIGHT, 5)
        self.assertEqual(set([0, 6]), set(indexes))

        board.reset()
        board.board[6] = KNIGHT
        indexes = board.piece_movements(KNIGHT, 6)
        self.assertEqual(set([1, 5]), set(indexes))

        board.reset()
        board.board[7] = KNIGHT
        indexes = board.piece_movements(KNIGHT, 7)
        self.assertEqual(set([0, 2]), set(indexes))

        board.reset()
        board.board[8] = KNIGHT
        indexes = board.piece_movements(KNIGHT, 8)
        self.assertEqual(set([1, 3]), set(indexes))

    def test_locate_king(self):
        board = Board(3, 3)
        pieces_counts = {'K': 4, 'Q': 0, 'B': 0, 'N': 0, 'R': 0}
        pieces = []
        for piece in PIECES_ORDER:
            pieces.extend([piece] * pieces_counts[piece])
        board.place_them_all(pieces=pieces)
        self.assertEqual(len(board.combinations), 1)
        self.assertEqual(set([0, 2, 6, 8]), set(map(lambda x: int(x.split('_')[1]),
                                                    list(board.combinations)[0].split(','))))

    def test_locate_queen(self):
        board = Board(3, 3)
        pieces_counts = {'K': 0, 'Q': 2, 'B': 0, 'N': 0, 'R': 0}
        pieces = []
        for piece in PIECES_ORDER:
            pieces.extend([piece] * pieces_counts[piece])
        board.place_them_all(pieces=pieces)
        self.assertEqual(len(board.combinations), 8)
        board.reset()
        board.combinations = set([])
        pieces_counts = {'K': 0, 'Q': 3, 'B': 0, 'N': 0, 'R': 0}
        pieces = []
        for piece in PIECES_ORDER:
            pieces.extend([piece] * pieces_counts[piece])
        board.place_them_all(pieces=pieces)
        self.assertEqual(len(board.combinations), 0)
