from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(board, row, col, n):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                    return False
                if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                    return False
            return True
        
        def backtrack(row, board, res, n):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            for col in range(n):
                if is_valid(board, row, col, n):
                    board[row][col] = 'Q'
                    backtrack(row + 1, board, res, n)
                    board[row][col] = '.'
        
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, board, res, n)
        return res
