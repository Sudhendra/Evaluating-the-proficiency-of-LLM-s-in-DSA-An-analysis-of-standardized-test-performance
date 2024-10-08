from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_not_under_attack(row, col, queens):
            return all(row != r and col != c and row - col != r - c and row + col != r + c for r, c in queens)

        def backtrack(queens, row):
            if row == n:
                result.append(queens)
                return
            for col in range(n):
                if is_not_under_attack(row, col, queens):
                    backtrack(queens + [(row, col)], row + 1)

        def format_solution(queens):
            board = [['.'] * n for _ in range(n)]
            for r, c in queens:
                board[r][c] = 'Q'
            return [''.join(row) for row in board]

        result = []
        backtrack([], 0)
        return [format_solution(sol) for sol in result]

# Example usage
solution = Solution()
print(solution.solveNQueens(4))  # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(solution.solveNQueens(1))  # Output: [["Q"]]
