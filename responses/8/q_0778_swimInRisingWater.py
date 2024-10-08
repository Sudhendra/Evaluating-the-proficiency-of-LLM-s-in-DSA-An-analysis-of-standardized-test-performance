from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        left, right = 0, n*n - 1
        while left < right:
            mid = (left + right) // 2
            visited = set()
            if self.canReachEnd(grid, n, 0, 0, mid, visited):
                right = mid
            else:
                left = mid + 1
        return left

    def canReachEnd(self, grid, n, i, j, t, visited):
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] > t or (i, j) in visited:
            return False
        if i == n - 1 and j == n - 1:
            return True

        visited.add((i, j))
        return (self.canReachEnd(grid, n, i+1, j, t, visited) or
                self.canReachEnd(grid, n, i-1, j, t, visited) or
                self.canReachEnd(grid, n, i, j+1, t, visited) or
                self.canReachEnd(grid, n, i, j-1, t, visited))
