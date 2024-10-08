from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def count_live_neighbors(row, col):
            count = 0
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n and abs(board[new_row][new_col]) == 1:
                    count += 1
            return count

        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                if board[i][j] == 1 and 2 <= live_neighbors <= 3:
                    board[i][j] = 1
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = -1

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

# Solution for the Game of Life problem
