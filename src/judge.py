from util import read_board
from solver import Solution
import time

fmt = "| {: ^20s} | {: ^11s} |"
print(fmt.format("testcases", "time"))
print(fmt.format("-"*18, "-"*11))

for i in range(10):
    file_path = f"../testcases/{i}.in"
    board = read_board(file_path)

    # Start timing
    start = time.monotonic()
    solution = Solution()
    solution.slidingPuzzle(board)
    time_cost = time.monotonic() - start
    print(fmt.format(f"testcases/{i}.in", f"{time_cost:.6f}"))
