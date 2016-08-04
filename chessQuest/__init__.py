from chessQuest.movements import left_right_cross, right_left_cross, horizontal, vertical, knight_move

FREE = 0
FORBIDDEN = 1

KING = 'K'
QUEEN = 'Q'
ROOK = 'R'
BISHOP = 'B'
KNIGHT = 'N'

PIECES_ORDER = [QUEEN, KING, ROOK, BISHOP, KNIGHT]

PIECES = {
    KING: {
        'movements': [left_right_cross(1), right_left_cross(1), horizontal(1), vertical(1)],
    },
    QUEEN: {
        'movements': [left_right_cross(), right_left_cross(), horizontal(), vertical()],
    },
    ROOK: {
        'movements': [horizontal(), vertical()],
    },
    BISHOP: {
        'movements': [left_right_cross(), right_left_cross()],
    },
    KNIGHT: {
        'movements': [knight_move]
    }
}
