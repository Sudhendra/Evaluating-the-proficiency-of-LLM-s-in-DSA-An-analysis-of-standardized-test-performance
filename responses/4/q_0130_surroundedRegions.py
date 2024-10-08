from typing import List

class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        def dfs(i, j):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
                board[i][j] = 'T'  # Temporary mark
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    dfs(x, y)
        
        # Mark 'O's on the border and their connected 'O's with 'T'
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0])-1)
        
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board)-1, j)
        
        # Flip 'O' to 'X' and restore 'T' to 'O'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
