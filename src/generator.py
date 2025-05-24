import random

def generate_puzzle():
    to_be_filled = list(range(0, 6))
    random.shuffle(to_be_filled)
    board = [to_be_filled[:3], to_be_filled[3:]]
    return board

if __name__ == "__main__":
    random.seed(3686)
    for idx in range(10):
        with open("../testcases/" + str(idx) + ".in", "w") as fout:
            board = generate_puzzle()
            for row in board:
                print("".join(map(str, row)), file=fout)