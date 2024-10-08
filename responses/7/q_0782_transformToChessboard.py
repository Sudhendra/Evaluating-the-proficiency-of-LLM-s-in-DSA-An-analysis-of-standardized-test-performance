class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Count the number of 1's and 0's in the first row and first column
        row_sum = sum(board[0])
        col_sum = sum(row[0] for row in board)
        
        # Check if it's possible to transform into a chessboard
        if row_sum != n // 2 and row_sum != (n + 1) // 2:
            return -1
        if col_sum != n // 2 and col_sum != (n + 1) // 2:
            return -1
        
        # Check if the board can be transformed into a valid chessboard
        for i in range(n):
            for j in range(n):
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) == 1:
                    return -1
        
        # Calculate the number of moves to transform into a chessboard
        row_diff = sum(board[0][j] != j % 2 for j in range(n))
        col_diff = sum(board[i][0] != i % 2 for i in range(n))
        
        if n % 2 == 1:
            if row_diff % 2 == 1:
                row_diff = n - row_diff
            if col_diff % 2 == 1:
                col_diff = n - col_diff
        
        return (row_diff + col_diff) // 2
