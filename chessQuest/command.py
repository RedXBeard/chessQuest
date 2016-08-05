from chessQuest import KING, QUEEN, ROOK, KNIGHT, BISHOP, PIECES_ORDER
from chessQuest.board import Board


def main():
    def take_counts(prompt, grater=False):
        data = input(prompt)
        while True:
            if str(data).isdigit():
                if grater and int(data) > 0:
                    break
                else:
                    break
            print("[!] Could not understand")
            data = input(prompt)
        return int(data)

    print("""
    Please give me board; width and height;
    """)

    len_x = take_counts("Board width ", True)
    len_y = take_counts("Board height ", True)

    print("""
    Please give me pieces' counts;
    """)

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

    board.place_them_all(pieces=pieces)
    board.show_combinations(limit=0)
    print("Combinations found in '{}'".format(board.spend_time))
