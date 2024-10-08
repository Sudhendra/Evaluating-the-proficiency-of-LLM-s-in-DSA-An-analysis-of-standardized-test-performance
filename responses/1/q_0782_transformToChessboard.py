class Solution:
    def movesToChessboard(self, board: List[List[int]) -> int:
        n = len(board)
        
        # Count the frequency of 0's and 1's in the first row and column
        row_0_count = board[0].count(0)
        col_0_count = sum(row[0] == 0 for row in board)
        row_diff = abs(row_0_count - (n - row_0_count))
        col_diff = abs(col_0_count - (n - col_0_count))
        
        # Check if the counts are valid for a chessboard
        if row_diff > 1 or col_diff > 1:
            return -1
        
        # Check if the counts result in alternating rows and columns
        if (n % 2 == 1 and (row_0_count % 2 == 1 or col_0_count % 2 == 1)) or (n % 2 == 0 and (row_0_count < n // 2 or col_0_count < n // 2)):
            return -1
        
        row_diff = n - row_diff if n % 2 == 1 and row_0_count % 2 == 1 else row_diff
        col_diff = n - col_diff if n % 2 == 1 and col_0_count % 2 == 1 else col_diff
        
        row_swaps = col_swaps = 0
        for i in range(n):
            if i % 2 == 0:
                row_swaps += 1 if board[i][0] == 0 else 0
                col_swaps += 1 if board[0][i] == 0 else 0
            else:
                row_swaps += 1 if board[i][0] == 1 else 0
                col_swaps += 1 if board[0][i] == 1 else 0
        
        if n % 2 == 1:
            if row_0_count % 2 == 1:
                row_swaps = n - row_swaps
            if col_0_count % 2 == 1:
                col_swaps = n - col_swaps
        
        return min(row_swaps, col_swaps) // 2