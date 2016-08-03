def left_right_cross(step=0):
    def inner(board, pointed_index):
        """
        To sign forbidden cells for positioned piece handler from left to right cross.
        :param board: board class object
        :param pointed_index: current position of piece
        :param step: one of more cell movement
        """
        to_left_top = []
        to_left_bottom = []
        pos_x = pointed_index % board.len_x
        pos_y = pointed_index / board.len_x

        counter = 1
        while True:
            index = pointed_index - counter * (board.len_x + 1)
            if index < 0 or index / board.len_x > pos_y or index % board.len_x > pos_x:
                break
            to_left_top.append(index)
            counter += 1
            if step:
                break

        counter = 1
        while True:
            index = pointed_index + counter * (board.len_x + 1)
            if index >= board.len_x * board.len_y or index / board.len_x < pos_y or index % board.len_x < pos_x:
                break
            to_left_bottom.append(index)
            counter += 1
            if step:
                break

        board.sign_indexes(to_left_bottom)
        board.sign_indexes(to_left_top)

    return inner


def right_left_cross(step=0):
    def inner(board, pointed_index):
        """
        To sign forbidden cells for positioned piece handler from right to left cross.
        :param board: board class object
        :param pointed_index: current position of piece
        :param step: one of more cell movement
        """
        to_right_top = []
        to_right_bottom = []
        pos_x = pointed_index % board.len_x
        pos_y = pointed_index / board.len_x

        counter = 1
        while True:
            index = pointed_index - counter * (board.len_x - 1)
            if index < 0 or index / board.len_x > pos_y or index % board.len_x < pos_x:
                break
            to_right_top.append(index)
            counter += 1
            if step:
                break

        counter = 1
        while True:
            index = pointed_index + counter * (board.len_x - 1)
            if index >= board.len_x * board.len_y or index / board.len_x < pos_y or index % board.len_x > pos_x:
                break
            to_right_bottom.append(index)
            counter += 1
            if step:
                break

        board.sign_indexes(to_right_bottom)
        board.sign_indexes(to_right_top)

    return inner


def horizontal(step=0):
    def inner(board, pointed_index):
        """
        To sign forbidden cells for positioned piece handler horizontally.
        :param board: board class object
        :param pointed_index: current position of piece
        :param step: one of more cell movement
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

        board.sign_indexes(indexes)

    return inner


def vertical(step=0):
    def inner(board, pointed_index):
        """
        To sign forbidden cells for positioned piece handler vertically.
        :param board: board class object
        :param pointed_index: current position of piece
        :param step: one of more cell movement
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

        while True:
            index -= board.len_x
            if index < 0:
                break
            if index != pointed_index:
                indexes.append(index)
            if step:
                break

        board.sign_indexes(indexes)

    return inner
