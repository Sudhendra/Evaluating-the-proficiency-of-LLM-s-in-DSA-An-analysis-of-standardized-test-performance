from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            # Check if there is a queen in the same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Check upper left diagonal
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check upper right diagonal
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def solve(board, row):
            if row == n:
                result.append(["".join(row) for row in board])
                return
            for i in range(n):
                if is_safe(board, row, i):
                    board[row][i] = 'Q'
                    solve(board, row + 1)
                    board[row][i] = '.'

        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        solve(board, 0)
        return result
