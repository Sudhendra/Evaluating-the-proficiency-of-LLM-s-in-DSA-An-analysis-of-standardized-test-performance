from typing import List

class Solution:
    
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            count = 1
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                count += dfs(i+di, j+dj)
            return count
        
        def is_connected_to_top(i, j):
            return i == 0
        
        def is_stable(i, j):
            return i < 0 or (0 <= i < m and 0 <= j < n and grid[i][j] == 2)
        
        def pre_process():
            for i, j in hits:
                grid[i][j] -= 1
                
        def post_process(i, j):
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if is_stable(ni, nj):
                    count = dfs(ni, nj)
                    if not is_connected_to_top(i, j):
                        count -= 1
                    res.append(max(0, count - 1))
            
        m, n = len(grid), len(grid[0])
        res = []
        
        pre_process()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
        
        for hit in reversed(hits):
            i, j = hit
            grid[i][j] += 1
            if grid[i][j] == 1:
                post_process(i, j)
        
        return res[::-1]
