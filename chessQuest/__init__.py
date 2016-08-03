from chessQuest.movements import left_right_cross, right_left_cross, horizontal, vertical

FREE = 0
FORBIDDEN = 1

KING = 'K'  # Sah
QUEEN = 'Q'  # Vezir
ROOK = 'R'  # Kale
BISHOP = 'B'  # Fil
KNIGHT = 'N'  # At

PIECES_ORDER = [QUEEN, ROOK, KNIGHT, KING]

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
    KNIGHT: {
        'movements': [left_right_cross(), right_left_cross()],
    }
}
