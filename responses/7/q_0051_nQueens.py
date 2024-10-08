from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_not_under_attack(row, col, rows, hills, dales):
            return not (rows[col] or hills[row - col] or dales[row + col])

        def place_queen(row, col, rows, hills, dales):
            rows[col] = 1
            hills[row - col] = 1
            dales[row + col] = 1

        def remove_queen(row, col, rows, hills, dales):
            rows[col] = 0
            hills[row - col] = 0
            dales[row + col] = 0

        def add_solution(n, rows):
            board = []
            for row in rows:
                board.append("".join(['Q' if i == row else '.' for i in range(n)]))
            result.append(board)

        def backtrack(row, rows, hills, dales):
            for col in range(n):
                if is_not_under_attack(row, col, rows, hills, dales):
                    place_queen(row, col, rows, hills, dales)
                    if row + 1 == n:
                        add_solution(n, rows)
                    else:
                        backtrack(row + 1, rows, hills, dales)
                    remove_queen(row, col, rows, hills, dales)

        result = []
        rows = [0] * n
        hills = [0] * (2 * n - 1)
        dales = [0] * (2 * n - 1)
        backtrack(0, rows, hills, dales)
        return result
