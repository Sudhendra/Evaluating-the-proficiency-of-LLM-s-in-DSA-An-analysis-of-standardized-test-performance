from typing import List

class Solution:
    
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]:
        
        def valid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        def is_border_element(i, j):
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                return True
            for ni, nj in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if valid(ni, nj) and grid[ni][nj] != grid[i][j]:
                    return True
            return False
        
        def dfs(i, j):
            if not valid(i, j) or grid[i][j] != target_color:
                return
            if is_border_element(i, j):
                result[i][j] = color
            else:
                result[i][j] = grid[i][j]
            grid[i][j] = -grid[i][j]
            for ni, nj in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                dfs(ni, nj)
        
        target_color = grid[row][col]
        result = [row[:] for row in grid]
        dfs(row, col)
        return result
