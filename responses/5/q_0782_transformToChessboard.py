from collections import Counter

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Check if the board is valid
        row_sum = sum(board[0])
        col_sum = sum(board[i][0] for i in range(n))
        for i in range(n):
            for j in range(n):
                if board[i][j] ^ board[0][0] ^ board[i][0] ^ board[0][j]:
                    return -1
        
        # Count the row and column patterns
        row_count = Counter(tuple(row) for row in board)
        col_count = Counter(tuple(board[i][j] for i in range(n)) for j in range(n))
        
        if len(row_count) != 2 or len(col_count) != 2:
            return -1
        
        row_keys = list(row_count.keys())
        col_keys = list(col_count.keys())
        
        if abs(row_count[row_keys[0]] - row_count[row_keys[1]]) > 1:
            return -1
        
        if abs(col_count[col_keys[0]] - col_count[col_keys[1]]) > 1:
            return -1
        
        # Calculate minimum moves based on row and col patterns
        first_row = row_keys[0]
        first_col = col_keys[0]
        
        diff_row = sum(first_row[i] != i % 2 for i in range(n))
        diff_col = sum(first_col[i] != i % 2 for i in range(n))
        
        if n % 2 == 0:
            return min(diff_row, n - diff_row) // 2 + min(diff_col, n - diff_col) // 2
        else:
            if row_count[first_row] % 2 != 0 or col_count[first_col] % 2 != 0:
                return -1
            return diff_row // 2 + diff_col // 2

# Time complexity: O(n^2)
# Space complexity: O(n)
