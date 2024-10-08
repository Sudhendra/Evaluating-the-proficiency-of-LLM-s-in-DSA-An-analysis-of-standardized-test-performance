from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def count_live_neighbors(i, j):
            live_count = 0
            for dx, dy in neighbors:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in (1, 2):
                    live_count += 1
            return live_count

        for i in range(m):
            for j in range(n):
                live_count = count_live_neighbors(i, j)
                if board[i][j] == 1 and (live_count < 2 or live_count > 3):
                    board[i][j] = 2
                elif board[i][j] == 0 and live_count == 3:
                    board[i][j] = 3

        for i in range(m):
            for j in range(n):
                board[i][j] %= 2
