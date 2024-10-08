from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def find_rook_position(board):
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R':
                        return i, j
        
        def count_pawns_in_direction(board, row, col, d_row, d_col):
            count = 0
            while 0 <= row < 8 and 0 <= col < 8:
                if board[row][col] == 'B':
                    break
                if board[row][col] == 'p':
                    count += 1
                    break
                row += d_row
                col += d_col
            return count

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        row, col = find_rook_position(board)
        captures = 0
        for d_row, d_col in directions:
            captures += count_pawns_in_direction(board, row+d_row, col+d_col, d_row, d_col)
        return captures