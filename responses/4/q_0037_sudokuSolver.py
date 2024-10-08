from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(num: str, row: int, col: int) -> bool:
            for i in range(9):
                if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True

        def solve() -> bool:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            if is_valid(k, i, j):
                                board[i][j] = k
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve()
