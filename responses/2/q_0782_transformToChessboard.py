class Solution:
    def movesToChessboard(self, board: List[List[int]) -> int:
        n = len(board)
        
        # Check if the board can be transformed into a valid chessboard
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] == 1:
                    return -1
        
        row_sum = sum(board[0])
        col_sum = sum(board[i][0] for i in range(n))
        
        row_diff = sum(abs(board[i][0] - i % 2) for i in range(n))
        col_diff = sum(abs(board[0][i] - i % 2) for i in range(n))
        
        if row_sum != n // 2 and row_sum != (n + 1) // 2:
            return -1
        if col_sum != n // 2 and col_sum != (n + 1) // 2:
            return -1
        
        if n % 2 == 1:
            if row_diff % 2 == 1 or col_diff % 2 == 1:
                return -1
            return min(row_diff // 2, n - row_diff // 2) // 2 + min(col_diff // 2, n - col_diff // 2) // 2
        
        return min(row_diff // 2, n - row_diff // 2) // 2 + min(col_diff // 2, n - col_diff // 2) // 2