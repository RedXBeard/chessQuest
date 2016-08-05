def cached(func):
    """
    cache decorator, to keep pieces movable cells indexes.
    :param func: board method.
    :return: wrapper function.
    """
    memo = {}

    def wrapper(board, *args):
        # chosen key as pieces representations
        # with possible cell index on board.
        key = "_".join(map(str, args))
        if key in memo:
            value = memo.get(key)
        else:
            value = func(board, *args)
            memo[key] = value
        return value
    return wrapper
