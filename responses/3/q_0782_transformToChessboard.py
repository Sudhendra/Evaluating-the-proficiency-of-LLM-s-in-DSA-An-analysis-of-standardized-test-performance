from collections import Counter

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)

        # Check if the board is valid chessboard
        row_counts = Counter(tuple(row) for row in board)
        col_counts = Counter(tuple(col) for col in zip(*board))
        if len(row_counts) != 2 or len(col_counts) != 2:
            return -1

        row_keys = list(row_counts.keys())
        col_keys = list(col_counts.keys())
        row1, row2 = row_keys
        col1, col2 = col_keys

        if abs(row_counts[row1] - row_counts[row2]) > 1 or abs(col_counts[col1] - col_counts[col2]) > 1:
            return -1

        diff_row = sum(board[0][i] != i % 2 for i in range(n))
        diff_col = sum(board[i][0] != i % 2 for i in range(n))

        if n % 2 == 1:
            if row_counts[row1] != n // 2 + n % 2 or col_counts[col1] != n // 2 + n % 2:
                return -1
            if row1[0] == col1[0]:
                return (diff_row + diff_col) // 2
            else:
                return (n - diff_row + n - diff_col) // 2
        else:
            if row_counts[row1] != n // 2 or col_counts[col1] != n // 2:
                return -1
            return min(diff_row, n - diff_row) // 2 + min(diff_col, n - diff_col) // 2
