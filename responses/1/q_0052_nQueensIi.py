class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col):
            return not (cols[col] or hill_diagonals[row - col] or dale_diagonals[row + col])

        def place_queen(row, col):
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row, col):
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def backtrack(row=0):
            nonlocal solutions
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        solutions += 1
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        solutions = 0
        backtrack()
        return solutions