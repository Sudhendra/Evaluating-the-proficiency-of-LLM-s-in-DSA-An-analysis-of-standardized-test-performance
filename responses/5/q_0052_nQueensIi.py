class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col, queens):
            return all(row != r and col != c and row + col != r + c and row - col != r - c for r, c in queens)

        def backtrack(row, queens):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if is_not_under_attack(row, col, queens):
                    queens.append((row, col))
                    backtrack(row + 1, queens)
                    queens.pop()

        count = 0
        backtrack(0, [])
        return count
