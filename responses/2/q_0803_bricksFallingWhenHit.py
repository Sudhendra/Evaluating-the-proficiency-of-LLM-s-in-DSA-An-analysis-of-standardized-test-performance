from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            count = 1
            count += sum(dfs(x, y) for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
            return count

        def is_stable(i, j):
            return i == 0 or any(grid[x][y] == 2 for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

        for i, j in hits:
            grid[i][j] -= 1

        for j in range(len(grid[0])):
            dfs(0, j)

        result = []
        for i in range(len(hits) - 1, -1, -1):
            x, y = hits[i]
            grid[x][y] += 1
            if grid[x][y] == 1 and is_stable(x, y):
                result.append(dfs(x, y) - 1)
            else:
                result.append(0)
        
        return result[::-1]
