from typing import List

class Solution:
    def isValid(self, board: List[List[str]], row: int, col: int, num: str) -> bool:
        for i in range(9):
            if board[row][i] == num or board[i][col] == num or board[3*(row//3)+i//3][3*(col//3)+i%3] == num:
                return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        def backtrack(row, col):
            if row == 9:
                return True
            if col == 9:
                return backtrack(row + 1, 0)
            if board[row][col] != '.':
                return backtrack(row, col + 1)

            for num in '123456789':
                if self.isValid(board, row, col, num):
                    board[row][col] = num
                    if backtrack(row, col + 1):
                        return True
                    board[row][col] = '.'

            return False

        backtrack(0, 0)
