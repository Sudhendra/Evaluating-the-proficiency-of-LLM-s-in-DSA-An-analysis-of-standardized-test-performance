class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col, diagonals, anti_diagonals):
            return row not in diagonals and row + col not in anti_diagonals and row - col not in diagonals

        def backtrack(row, diagonals, anti_diagonals):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if is_not_under_attack(row, col, diagonals, anti_diagonals):
                    diagonals.add(row)
                    anti_diagonals.add(row + col)
                    backtrack(row + 1, diagonals, anti_diagonals)
                    diagonals.remove(row)
                    anti_diagonals.remove(row + col)

        count = 0
        diagonals = set()
        anti_diagonals = set()
        backtrack(0, diagonals, anti_diagonals)
        return count