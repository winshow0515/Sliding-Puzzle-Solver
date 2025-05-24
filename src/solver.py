from collections import deque
from copy import deepcopy
from typing import List

class Solution:
    def isEnd(self, board):
        return board == [[1, 2, 3], [4, 5, 0]]

    def getPossibilities(self, board):
        # Find Zero
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    x, y = i, j
        possibilities = []
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x+dx, y+dy
            if not(0 <= nx <= 1 and 0 <= ny <= 2):
                continue
            next_board = deepcopy(board)
            next_board[nx][ny], next_board[x][y] = next_board[x][y], next_board[nx][ny]
            possibilities.append(next_board)
        return possibilities
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        Q = deque([(board, 0)])
        visit = set()
        while Q:
            cur_board, cost = Q.popleft()
            if self.isEnd(cur_board):
                return cost
            key = str(cur_board)
            if key in visit:
                continue
            visit.add(key)
            for nxt_board in self.getPossibilities(cur_board):
                Q.append((nxt_board, cost+1))
        return -1