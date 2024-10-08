from collections import Counter

class Solution:
    
    def movesToChessboard(self, board: List[List[int]) -> int:
        n = len(board)
        
        # Check if the initial board is valid
        row_counts = Counter(tuple(row) for row in board)
        col_counts = Counter(tuple(col) for col in zip(*board))
        
        if len(row_counts) != 2 or len(col_counts) != 2:
            return -1
        
        x, y = row_counts
        a, b = col_counts
        
        if abs(x - y) > 1 or abs(a - b) > 1:
            return -1
        
        row1, row2 = [list(row) for row, _ in sorted(row_counts.items(), key=lambda x: x[1], reverse=True)]
        col1, col2 = [list(col) for col, _ in sorted(col_counts.items(), key=lambda x: x[1], reverse=True)]
        
        if any(x ^ y ^ row1[0] ^ row1[1] for x, y in zip(row1, row2)) or any(a ^ b ^ col1[0] ^ col1[1] for a, b in zip(col1, col2)):
            return -1
        
        return sum(board[0][0] != row1[i] for i in range(n // 2)) + sum(board[i][0] != row1[i % 2] for i in range(n))
