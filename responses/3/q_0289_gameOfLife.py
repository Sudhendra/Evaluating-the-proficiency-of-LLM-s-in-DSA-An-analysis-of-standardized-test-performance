from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board:
            return
        
        def count_live_neighbors(board, i, j):
            count = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            for dx, dy in directions:
                new_x, new_y = i+dx, j+dy
                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and abs(board[new_x][new_y]) == 1:
                    count += 1
            return count
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(board, i, j)
                
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0