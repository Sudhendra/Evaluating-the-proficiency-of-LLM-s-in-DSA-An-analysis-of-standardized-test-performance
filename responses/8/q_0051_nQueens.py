from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                    return False
            return True
        
        def solve(board, row):
            if row == n:
                result.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in board])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(board, row + 1)

        result = []
        solve([0] * n, 0)
        return result
