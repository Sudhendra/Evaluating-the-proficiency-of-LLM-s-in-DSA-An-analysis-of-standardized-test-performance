from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def is_stable(i, j):
            if i == 0:
                return True
            for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) in stable_bricks:
                    return True
            return False

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] == 1 and (i, j) not in visited):
                return 0
            visited.add((i, j))
            return 1 + sum(dfs(ni, nj) for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

        def is_connected_to_top():
            return i == 0

        m, n = len(grid), len(grid[0])
        for i, j in hits:
            grid[i][j] -= 1

        stable_bricks = set([(i, j) for j in range(n) if grid[0][j] == 1 for i in range(m)]
        for i, j in stable_bricks:
            dfs(i, j)

        result = []
        for i, j in reversed(hits):
            grid[i][j] += 1
            if grid[i][j] == 1 and is_stable(i, j):
                brick_count = dfs(i, j) - 1
                stable_bricks.add((i, j))
            else:
                brick_count = 0
            result.append(brick_count)

        return result[::-1]