from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # Union find functions
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return
            parent[root_x] = root_y
            size[root_y] += size[root_x]

        def is_connected(x, y):
            return find(x) == find(y)

        # Direction vectors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        m, n = len(grid), len(grid[0])
        parent = [i for i in range(m * n)]
        size = [1] * (m * n)
        
        def index(x, y):
            return x * n + y
        
        for i, j in hits:
            grid[i][j] -= 1

        for i in range(n):
            if grid[0][i] == 1:
                union(i, m * n)

        for i in range(1, m):
            for j in range(n):
                if grid[i][j] == 1:
                    if grid[i - 1][j] == 1:
                        union(index(i, j), index(i - 1, j))
                    if j > 0 and grid[i][j - 1] == 1:
                        union(index(i, j), index(i, j - 1))

        result = []
        for i, j in reversed(hits):
            pre_fallen = size[find(m * n)]
            if grid[i][j] == 0:
                result.append(0)
            else:
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                        union(index(i, j), index(ni, nj))
                if i == 0:
                    size[find(index(i, j))] += 1
                grid[i][j] = 1
                result.append(max(0, size[find(m * n)] - pre_fallen - 1))

        return result[::-1]
