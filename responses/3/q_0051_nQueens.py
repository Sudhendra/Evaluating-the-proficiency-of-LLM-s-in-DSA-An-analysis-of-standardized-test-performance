from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                    return False
            return True

        def backtrack(board, row, result):
            if row == n:
                result.append(["".join(["Q" if col == board[row] else "." for col in range(n)]) for row in range(n)])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1, result)

        result = []
        backtrack([0]*n, 0, result)
        return result
