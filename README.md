# Chess Quest
Find all unique configurations of a set of normal chess pieces on a chess board with dimensions M×N where none of the pieces is in a position to take any of the others. Assume the colour of the piece does not matter, and that there are no pawns among the pieces.

## Usage

A little info;

    'K' -> King
    'Q' -> Queen
    'B' -> Bishop
    'N' -> Knight
    'R' -> Rook

### As terminal script

run the following line

    $> python main.py
    
then follow the steps which are asked.

### On python console

Type followings;

    from chessQuest import PIECES, PIECES_ORDER, KNIGHT, KING, QUEEN, ROOK, BISHOP
    from chessQuest.board import Board
                                      
    board = Board(7, 7)
    pieces_counts = {'K': 2, 'Q': 2, 'B': 2, 'N': 1}
    pieces = []
    for piece in PIECES_ORDER:
        pieces.extend([piece] * pieces_counts[piece])
    board.place_them_all(pieces=pieces)
    
    # To get the count
    board.show_combinations(limit=0)
    # Or to get some of them
    board.show_combinations(limit=10)


Thank you.