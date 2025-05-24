def read_board(path):
    with open(path, "r") as f:
        board = [list(map(int, line.strip())) for line in f.readlines()]
    return board