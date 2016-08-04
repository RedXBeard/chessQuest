def left_right_cross(step=0):
    """
    :param step: one of more cell movement
    :return: function
    """
    def inner(board, pointed_index):
        """
        To sign forbidden cells for positioned piece handler from left to right cross.
        :param board: Board class object
        :param pointed_index: current position of piece
        :return: Boolean acceptable or not
        """
        indexes = []
        pos_x = pointed_index % board.len_x
        pos_y = pointed_index / board.len_x

        counter = 1
        while True:
            index = pointed_index - counter * (board.len_x + 1)
            if index < 0 or index / board.len_x > pos_y or index % board.len_x > pos_x:
                break
            indexes.append(index)
            counter += 1
            if step:
                break

        counter = 1
        while True:
            index = pointed_index + counter * (board.len_x + 1)
            if index >= board.len_x * board.len_y or index / board.len_x < pos_y or index % board.len_x < pos_x:
                break
            indexes.append(index)
            counter += 1
            if step:
                break

        return board.sign_indexes(indexes)

    return inner


def right_left_cross(step=0):
    """
    :param step: one of more cell movement
    :return: function
    """
    def inner(board, pointed_index):
        """
        To sign forbidden cells for positioned piece handler from right to left cross.
        :param board: Board class object
        :param pointed_index: current position of piece
        :return: Boolean acceptable or not
        """
        indexes = []
        pos_x = pointed_index % board.len_x
        pos_y = pointed_index / board.len_x

        counter = 1
        while True:
            index = pointed_index - counter * (board.len_x - 1)
            if index < 0 or index / board.len_x > pos_y or index % board.len_x < pos_x:
                break
            indexes.append(index)
            counter += 1
            if step:
                break

        counter = 1
        while True:
            index = pointed_index + counter * (board.len_x - 1)
            if index >= board.len_x * board.len_y or index / board.len_x < pos_y or index % board.len_x > pos_x:
                break
            indexes.append(index)
            counter += 1
            if step:
                break

        return board.sign_indexes(indexes)

    return inner


def horizontal(step=0):
    """
    :param step: one of more cell movement
    :return: function
    """
    def inner(board, pointed_index):
        """
        To sign forbidden cells for positioned piece handler horizontally.
        :param board: Board class object
        :param pointed_index: current position of piece
        :return: Boolean acceptable or not
        """
        indexes = []
        index = pointed_index
        while True:
            index += 1
            if index % board.len_x == 0:
                break
            indexes.append(index)
            if step:
                break

        index = pointed_index
        while True:
            index -= 1
            if index % board.len_x == board.len_x - 1:
                break
            indexes.append(index)
            if step:
                break

        return board.sign_indexes(indexes)

    return inner


def vertical(step=0):
    """
    :param step: one of more cell movement
    :return: function
    """
    def inner(board, pointed_index):
        """
        To sign forbidden cells for positioned piece handler vertically.
        :param board: Board class object
        :param pointed_index: current position of piece
        :return: Boolean acceptable or not
        """
        indexes = []
        max_index = board.len_x * board.len_y - 1
        index = pointed_index
        while True:
            index += board.len_x
            if index > max_index:
                break
            if index != pointed_index:
                indexes.append(index)
            if step:
                break

        index = pointed_index
        while True:
            index -= board.len_x
            if index < 0:
                break
            if index != pointed_index:
                indexes.append(index)
            if step:
                break

        return board.sign_indexes(indexes)

    return inner


def knight_move(board, pointed_index):
    """
    Detect all movement positions and their availability.
    :param board: Board class object
    :param pointed_index: current position of piece
    :return: Boolean acceptable or not
    """

    indexes = []

    pos_y = pointed_index / board.len_x

    top_left_index = pointed_index - 1 - board.len_x * 2
    top_right_index = pointed_index + 1 - board.len_x * 2
    bottom_left_index = pointed_index - 1 + board.len_x * 2
    bottom_right_index = pointed_index + 1 + board.len_x * 2

    left_top_index = pointed_index - 2 - board.len_x
    left_bottom_index = pointed_index - 2 + board.len_x
    right_top_index = pointed_index + 2 - board.len_x
    right_bottom_index = pointed_index + 2 + board.len_x

    if top_left_index >= 0 and pos_y - top_left_index / board.len_x == 2:
        indexes.append(top_left_index)
    if top_right_index >= 0 and pos_y - top_right_index / board.len_x == 2:
        indexes.append(top_right_index)
    if bottom_left_index < board.len_x * board.len_y and bottom_left_index / board.len_x - pos_y == 2:
        indexes.append(bottom_left_index)
    if bottom_right_index < board.len_x * board.len_y and bottom_right_index / board.len_x - pos_y == 2:
        indexes.append(bottom_right_index)

    if left_top_index >= 0 and pos_y - left_top_index / board.len_x == 1:
        indexes.append(left_top_index)
    if left_bottom_index < board.len_x * board.len_y and left_bottom_index / board.len_x - pos_y == 1:
        indexes.append(left_bottom_index)
    if right_top_index >= 0 and pos_y - right_top_index / board.len_x == 1:
        indexes.append(right_top_index)
    if right_bottom_index < board.len_x * board.len_y and right_bottom_index / board.len_x - pos_y == 1:
        indexes.append(right_bottom_index)

    return board.sign_indexes(indexes)
