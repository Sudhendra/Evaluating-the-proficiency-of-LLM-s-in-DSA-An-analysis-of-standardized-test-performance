from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                    return False
                if col + (row - i) < len(board) and board[i][col + (row - i)] == 'Q':
                    return False
            return True

        def backtrack(row):
            nonlocal res, board
            if row == len(board):
                res.append(["".join(row) for row in board])
                return
            for col in range(len(board)):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0)
        return res
