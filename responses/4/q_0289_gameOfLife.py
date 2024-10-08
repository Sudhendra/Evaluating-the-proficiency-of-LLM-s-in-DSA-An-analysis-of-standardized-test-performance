from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board:
            return
        
        m, n = len(board), len(board[0])

        def count_live_neighbors(board, i, j):
            count = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in (1, 2):
                    count += 1
            return count

        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(board, i, j)
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 2  # 1 -> 0 (mark as dead)
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 3  # 0 -> 1 (mark as live)

        for i in range(m):
            for j in range(n):
                board[i][j] %= 2  # updating states

# Time complexity: O(m*n) where m is the number of rows and n is the number of columns.
# Space complexity: O(1)
