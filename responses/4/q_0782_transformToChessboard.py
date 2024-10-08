from collections import Counter

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Count the occurrences of the first row and first column
        row_counts = Counter(tuple(row) for row in board)
        col_counts = Counter(tuple(col) for col in zip(*board))
        
        if len(row_counts) != 2 or len(col_counts) != 2:
            return -1
        
        # Check if the number of ones and zeros are equal in both rows and columns
        row_keys = list(row_counts.keys())
        col_keys = list(col_counts.keys())
        if abs(row_keys[0].count(1) - row_keys[1].count(1)) > 1 or abs(col_keys[0].count(1) - col_keys[1].count(1)) > 1:
            return -1
        
        # Check if the board is a valid chessboard pattern
        if any(row_counts[row] != n // 2 for row in row_counts):
            return -1
        if any(col_counts[col] != n // 2 for col in col_counts):
            return -1
        
        # Find the minimum number of swaps
        row_xor = (row_keys[0][0] ^ col_keys[0][0])
        swaps_row = sum(not all(x ^ y == row_xor for x, y in zip(row, row[1:])) for row in board)
        swaps_col = sum(not all(x ^ y == row_xor for x, y in zip(col, col[1:])) for col in zip(*board))
        
        return min(swaps_row, swaps_col) // 2
