from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])

        def dfs(i, j):
            if 0 <= i < rows and 0 <= j < cols and board[i][j] == 'O':
                board[i][j] = 'T'
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)

        for j in range(cols):
            dfs(0, j)
            dfs(rows-1, j)

        for i in range(rows):
            for j in range(cols):
                board[i][j] = 'X' if board[i][j] == 'O' else 'O'
                board[i][j] = 'O' if board[i][j] == 'T' else board[i][j]

        return
