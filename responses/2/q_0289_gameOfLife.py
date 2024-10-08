from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def count_live_neighbors(board, i, j):
            live_count = 0
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and (board[ni][nj] == 1 or board[ni][nj] == -1):
                    live_count += 1
            
            return live_count
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(board, i, j)
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] == 2 or board[i][j] == 1 else 0
