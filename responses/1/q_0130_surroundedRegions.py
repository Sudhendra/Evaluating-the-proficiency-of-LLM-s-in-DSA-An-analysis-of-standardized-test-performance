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
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                dfs(i+dx, j+dy)

        # Step 1: Mark connected 'O's on borders as 'T'
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        # Step 2: Flip 'T's back to 'O', and 'O's to 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
