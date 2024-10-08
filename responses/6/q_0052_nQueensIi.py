class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row: int, col: int, queens: list) -> bool:
            for r, c in queens:
                if r == row or c == col or abs(r - row) == abs(c - col):
                    return False
            return True

        def backtrack(row: int, queens: list, count: list):
            if row == n:
                count[0] += 1
                return
            for col in range(n):
                if is_not_under_attack(row, col, queens):
                    queens.append((row, col))
                    backtrack(row + 1, queens, count)
                    queens.pop()

        count = [0]
        backtrack(0, [], count)
        return count[0]
