from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 2
                islands.append((i, j))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dfs(i + dx, j + dy)
        
        def first_island():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        return
    
        def expand():
            level = 0
            while islands:
                size = len(islands)
                for _ in range(size):
                    i, j = islands.popleft()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                            if grid[x][y] == 1:
                                return level
                            elif grid[x][y] == 0:
                                grid[x][y] = 2
                                islands.append((x, y))
                level += 1
        
        islands = deque()
        
        first_island()
        
        return expand()
