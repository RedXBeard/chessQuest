# Chess Quest
Find all unique configurations of a set of normal chess pieces on a chess board with dimensions M×N where none of the pieces is in a position to take any of the others. Assume the colour of the piece does not matter, and that there are no pawns among the pieces.

## Info

With caching spending time is decreased almost `40%`. Calculation completion time depends on machine capability, tested results for specified test case as following;

|Machine | Specifications | Calculation Time |
| ------------- | ------------- | ------------- |
|MacBook Air 10.11.5| 1.4Ghz i5 8GB DDR3| 22 - 25sec.|
|Linux Mint 17.3| 2.4Ghz i7 12GB DDR3| 12 - 14sec.|
## Usage

A little info;

    'K' -> King
    'Q' -> Queen
    'B' -> Bishop
    'N' -> Knight
    'R' -> Rook

### As console script

` [ Warning ] ` Be sure you are using last version of `pip` and `setuptools`

Just type the following to install, in source folder, then run;

    $> pip[2.7, 3] install -e .
    $> # To run; 
    $> # According to the terminal app, 
    $> # when the following line typed, 
    $> # folder can be changed, so you should type again
    $> chessquest

Then follow the prompts on screen.

### As terminal script

Run the following line

    $> python main.py
    
then follow the steps which are asked.

### On python console

Type followings;

    from chessQuest import PIECES, PIECES_ORDER, KNIGHT, KING, QUEEN, ROOK, BISHOP
    from chessQuest.board import Board
                                      
    board = Board(7, 7)
    pieces_counts = {'K': 2, 'Q': 2, 'B': 2, 'N': 1, 'R': 0}
    pieces = []
    for piece in PIECES_ORDER:
        pieces.extend([piece] * pieces_counts[piece])
    board.place_them_all(pieces=pieces)
    
    # To get the count
    board.show_combinations(limit=0)
    # Or to get some of them
    board.show_combinations(limit=10)
    # To get time that spend
    board.spend_time


Thank you.