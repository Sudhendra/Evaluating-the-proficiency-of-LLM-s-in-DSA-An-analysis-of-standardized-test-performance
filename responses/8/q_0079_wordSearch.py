from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        rows = len(board)
        cols = len(board[0])
        
        def dfs(row, col, idx):
            if idx == len(word):
                return True

            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[idx]:
                return False
            
            tmp = board[row][col]
            board[row][col] = "#"
            
            res = dfs(row+1, col, idx+1) or dfs(row-1, col, idx+1) or dfs(row, col+1, idx+1) or dfs(row, col-1, idx+1)
            
            board[row][col] = tmp
            
            return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False
