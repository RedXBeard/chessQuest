from chessQuest import PIECES_ORDER, KNIGHT, KING, QUEEN, ROOK, BISHOP
from chessQuest.board import Board


def take_counts(prompt):
    while True:
        data = input(prompt)
        if str(data).isdigit():
            break
        print("[!] Could not understand")
    return data

if __name__ == '__main__':
    print """
    Please give me board width and height;
    """

    len_x = take_counts("Board width ")
    len_y = take_counts("Board height ")

    print """
    Please give me pieces' counts;
    """

    pieces_counts = {}
    pieces_counts.setdefault(KING, take_counts("King count? "))
    pieces_counts.setdefault(QUEEN, take_counts("Queen count? "))
    pieces_counts.setdefault(ROOK, take_counts("Rook count? "))
    pieces_counts.setdefault(KNIGHT, take_counts("Knight count? "))
    pieces_counts.setdefault(BISHOP, take_counts("Bishop count? "))

    board = Board(len_x, len_y)
    pieces = []

    for piece in PIECES_ORDER:
        pieces.extend([piece] * pieces_counts[piece])

    print pieces
