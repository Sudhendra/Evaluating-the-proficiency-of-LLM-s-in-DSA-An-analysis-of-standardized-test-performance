from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + x, j + y)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(1, n - 1):
            dfs(0, j)
            dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
