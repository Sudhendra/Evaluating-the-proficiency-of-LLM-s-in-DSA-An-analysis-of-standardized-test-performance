class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_valid(board, row, col, n):
            for i in range(row):
                if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                    return False
            return True

        def backtrack(board, row, n):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if is_valid(board, row, col, n):
                    board[row] = col
                    count += backtrack(board, row + 1, n)
                    board[row] = 0
            return count

        return backtrack([0]*n, 0, n)
