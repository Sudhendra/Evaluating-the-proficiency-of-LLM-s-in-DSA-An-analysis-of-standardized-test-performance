from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_row, rook_col = 0, 0

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_row, rook_col = i, j
                    break

        captures = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in directions:
            x, y = rook_row + dx, rook_col + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'B':
                    break
                if board[x][y] == 'p':
                    captures += 1
                    break
                x += dx
                y += dy
        
        return captures
