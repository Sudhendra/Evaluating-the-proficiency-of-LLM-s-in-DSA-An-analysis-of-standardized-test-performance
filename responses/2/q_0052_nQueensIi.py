class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_valid(board, row, col):
            for i in range(row):
                if board[i] == col or abs(i - row) == abs(board[i] - col):
                    return False
            return True
        
        def dfs(board, row):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    dfs(board, row+1)
                    board[row] = 0
        
        count = 0
        board = [0] * n
        dfs(board, 0)
        return count