from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def find_rook_position(board):
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R':
                        return (i, j)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rook_pos = find_rook_position(board)
        count = 0

        for dx, dy in directions:
            x, y = rook_pos
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p':
                    count += 1
                    break
                if board[x][y] == 'B':
                    break
                x += dx
                y += dy

        return count
