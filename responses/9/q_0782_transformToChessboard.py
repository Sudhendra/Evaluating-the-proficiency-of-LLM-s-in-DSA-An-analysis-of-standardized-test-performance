from typing import List

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        row_sum = sum(board[0])
        col_sum = sum(board[i][0] for i in range(n))
        row_diff = col_diff = row_cnt = col_cnt = 0

        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1
                
        for i in range(n):
            row_diff += board[i][0] == i % 2
            col_diff += board[0][i] == i % 2
            row_cnt += board[i][0]
            col_cnt += board[0][i]
        
        if not n // 2 <= row_sum <= (n + 1) // 2 or not n // 2 <= col_sum <= (n + 1) // 2:
            return -1
        if row_cnt != n // 2 and row_cnt != (n + 1) // 2 or col_cnt != n // 2 and col_cnt != (n + 1) // 2:
            return -1
        if n % 2 == 1:
            if row_diff % 2 == 1 or col_diff % 2 == 1:
                return -1
            return row_diff // 2 + col_diff // 2
        else:
            return min(n // 2 - row_diff + n % 2 * (row_diff % 2), n // 2 - col_diff + n % 2 * (col_diff % 2))

# Example test cases
sol = Solution()
board1 = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
board2 = [[0,1],[1,0]]
board3 = [[1,0],[1,0]]
print(sol.movesToChessboard(board1))  # Output: 2
print(sol.movesToChessboard(board2))  # Output: 0
print(sol.movesToChessboard(board3))  # Output: -1
