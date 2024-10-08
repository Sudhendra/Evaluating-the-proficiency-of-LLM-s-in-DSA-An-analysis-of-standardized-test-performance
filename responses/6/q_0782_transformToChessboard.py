from collections import Counter
from typing import List

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Check if the board could be a valid chessboard
        rows = [tuple(row) for row in board]
        cols = [tuple(col) for col in zip(*board)]
        row_counter = Counter(rows)
        col_counter = Counter(cols)
        if len(row_counter) != 2 or len(col_counter) != 2:
            return -1
        if abs(row_counter.most_common(2)[0][1] - row_counter.most_common(2)[1][1]) > 1:
            return -1
        if abs(col_counter.most_common(2)[0][1] - col_counter.most_common(2)[1][1]) > 1:
            return -1
        
        row_xor = [sum(row[i] == i % 2 for i in range(n)) for row in board]
        col_xor = [sum(col[i] == i % 2 for i in range(n)) for col in zip(*board)]
        
        row_swap_diff = sum(row_xor) // 2
        col_swap_diff = sum(col_xor) // 2
        
        return min(row_swap_diff, n - row_swap_diff) + min(col_swap_diff, n - col_swap_diff)
