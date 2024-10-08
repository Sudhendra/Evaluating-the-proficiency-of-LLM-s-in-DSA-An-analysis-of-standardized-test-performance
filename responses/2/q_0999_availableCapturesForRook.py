class Solution:
    def numRookCaptures(self, board: List[List[str]) -> int:
        def find_rook(board):
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R':
                        return (i, j)

        def capture_pawn(board, r, c, dr, dc):
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 'p':
                    return 1
                if board[r][c] == 'B':
                    return 0
                r += dr
                c += dc
            return 0

        rook_pos = find_rook(board)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        captures = 0

        for dr, dc in directions:
            captures += capture_pawn(board, rook_pos[0] + dr, rook_pos[1] + dc, dr, dc)

        return captures