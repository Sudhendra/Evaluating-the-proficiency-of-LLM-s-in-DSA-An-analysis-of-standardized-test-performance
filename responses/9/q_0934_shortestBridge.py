from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j, n, visited, island):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1 or visited[i][j]:
                return
            visited[i][j] = True
            island.append((i, j))
            dfs(grid, i+1, j, n, visited, island)
            dfs(grid, i-1, j, n, visited, island)
            dfs(grid, i, j+1, n, visited, island)
            dfs(grid, i, j-1, n, visited, island)

        def bfs(grid, island, n):
            q = []
            for i, j in island:
                q.append((i, j, 0))
            visited = set(island)
            while q:
                i, j, step = q.pop(0)
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                        if grid[x][y] == 1:
                            return step
                        q.append((x, y, step+1))
                        visited.add((x, y))

        n = len(grid)
        found = False
        visited = [[False]*n for _ in range(n)]
        island1 = []
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(grid, i, j, n, visited, island1)
                    found = True

        return bfs(grid, island1, n)

# Example usage
grid = [[0,1],[1,0]]
sol = Solution()
print(sol.shortestBridge(grid))  # Output: 1
```
