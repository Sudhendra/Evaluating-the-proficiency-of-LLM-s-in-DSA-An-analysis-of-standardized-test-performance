from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_not_under_attack(row, col, queens):
            return all(row != r and col != c and row - col != r - c and row + col != r + c for r, c in queens)
        
        def backtrack(row, queens):
            if row == n:
                result.append([''.join(['Q' if (i, j) in queens else '.' for j in range(n)]) for i in range(n)]
                return
            for col in range(n):
                if is_not_under_attack(row, col, queens):
                    backtrack(row + 1, queens + [(row, col)])
        
        result = []
        backtrack(0, [])
        return result
