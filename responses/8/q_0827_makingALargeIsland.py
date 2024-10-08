from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, index):
            if not (0 <= i < n and 0 <= j < n) or grid[i][j] != 1:
                return 0
            grid[i][j] = index
            return 1 + sum(dfs(i + x, j + y, index) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)])

        def check_connectivity(i, j):
            neighbors = set()
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + x < n and 0 <= j + y < n:
                    neighbors.add(grid[i + x][j + y])
            return sum(areas[neighbor] for neighbor in neighbors)

        n = len(grid)
        areas = {0: 0}
        index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[index] = dfs(i, j, index)
                    index += 1

        res = max(areas.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    res = max(res, 1 + check_connectivity(i, j))

        return min(res, n*n)

# Example usage
solution = Solution()
grid = [[1, 0], [0, 1]]
print(solution.largestIsland(grid))  # Output: 3
