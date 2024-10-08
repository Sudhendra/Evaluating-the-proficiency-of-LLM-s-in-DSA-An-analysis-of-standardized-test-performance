from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_pos = [(i, row.index('R')) for i, row in enumerate(board) if 'R' in row][0]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        captures = 0

        for dx, dy in directions:
            x, y = rook_pos[0], rook_pos[1]
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p':
                    captures += 1
                    break
                elif board[x][y] == 'B':
                    break
                x += dx
                y += dy

        return captures
