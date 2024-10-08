from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]) -> int:
        def find_rook_position(board):
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R':
                        return (i, j)
            return None

        def capture_pawns(board, row, col):
            count = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in directions:
                x, y = row + dx, col + dy
                while 0 <= x < 8 and 0 <= y < 8:
                    if board[x][y] == 'p':
                        count += 1
                        break
                    elif board[x][y] == 'B':
                        break
                    x += dx
                    y += dy

            return count

        rook_position = find_rook_position(board)
        if rook_position is None:
            return 0

        return capture_pawns(board, rook_position[0], rook_position[1])
