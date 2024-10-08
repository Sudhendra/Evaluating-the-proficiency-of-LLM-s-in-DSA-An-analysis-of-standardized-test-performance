from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def find_rook_position(board):
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R':
                        return (i, j)

        rook_pos = find_rook_position(board)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        captures = 0

        for direction in directions:
            x, y = rook_pos
            dx, dy = direction

            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p':
                    captures += 1
                    break
                elif board[x][y] == 'B':
                    break

                x += dx
                y += dy

        return captures
