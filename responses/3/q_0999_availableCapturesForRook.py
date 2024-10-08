from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_row, rook_col = 0, 0
        count = 0
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_row, rook_col = i, j
                    break
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for d_row, d_col in directions:
            row, col = rook_row + d_row, rook_col + d_col
            while 0 <= row < 8 and 0 <= col < 8:
                if board[row][col] == 'p':
                    count += 1
                if board[row][col] != '.':
                    break
                row, col = row + d_row, col + d_col
        
        return count
