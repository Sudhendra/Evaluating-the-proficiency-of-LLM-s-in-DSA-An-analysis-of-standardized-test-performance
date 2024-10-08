from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def dfs(i, j, index):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = index
                return 1 + sum(dfs(i+1, j, index), dfs(i-1, j, index), dfs(i, j+1, index), dfs(i, j-1, index))
            return 0
        
        sizes = {0: 0}  # island index to size
        
        index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    sizes[index] = dfs(i, j, index)
                    index += 1
        
        max_area = max(sizes.values())
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    island_ids = set()
                    for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                        if 0 <= ni < n and 0 <= nj < n:
                            island_ids.add(grid[ni][nj])
                    max_area = max(max_area, 1 + sum(sizes[id] for id in island_ids))
        
        return max_area