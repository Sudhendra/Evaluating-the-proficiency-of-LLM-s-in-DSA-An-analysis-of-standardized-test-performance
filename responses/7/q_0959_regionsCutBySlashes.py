from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = 3 * n
        parent = [i for i in range(size)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for i in range(n):
            for j in range(n):
                base = 3 * (n * i + j)
                if grid[i][j] == "/":
                    union(base, base + 1)
                    union(base + 2, base + 3)
                elif grid[i][j] == "\\":
                    union(base + 1, base + 2)
                    union(base, base + 3)
                else:
                    union(base, base + 1)
                    union(base + 1, base + 2)
                    union(base + 2, base + 3)
                if i < n - 1:
                    union(base + 2, base + 3 + 3 * n)
                if j < n - 1:
                    union(base + 1, base + 2 + 3)

        regions = 0
        for i in range(size):
            if parent[i] == i:
                regions += 1

        return regions
