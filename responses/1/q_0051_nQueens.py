class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                    return False
                if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                    return False
            return True
        
        def backtrack(row):
            if row == n:
                solution = [''.join(row) for row in board]
                result.append(solution)
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'
        
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0)
        
        return result
