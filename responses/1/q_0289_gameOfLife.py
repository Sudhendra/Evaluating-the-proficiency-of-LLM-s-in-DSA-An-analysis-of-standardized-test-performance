from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board or not board[0]:
            return
        
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        
        def count_live_neighbors(x, y):
            live_neighbors = 0
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and abs(board[new_x][new_y]) == 1:
                    live_neighbors += 1
            return live_neighbors
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbors = count_live_neighbors(i, j)
                
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
