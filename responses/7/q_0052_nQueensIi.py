class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(board, row, col):
            for i in range(col):
                if board[row][i] == 1:
                    return False
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False
            for i, j in zip(range(row, n, 1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False
            return True

        def solve_nqueens(board, col):
            if col >= n:
                return 1
            count = 0
            for i in range(n):
                if is_safe(board, i, col):
                    board[i][col] = 1
                    count += solve_nqueens(board, col+1)
                    board[i][col] = 0
            return count

        board = [[0 for _ in range(n)] for _ in range(n)]
        return solve_nqueens(board, 0)
