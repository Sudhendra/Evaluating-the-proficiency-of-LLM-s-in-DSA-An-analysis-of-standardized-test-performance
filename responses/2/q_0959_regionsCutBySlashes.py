from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                parent[root_x] = root_y

        n = len(grid)
        size = n * n * 4
        parent = [i for i in range(size)]

        for i in range(n):
            for j in range(n):
                base = 4 * (i * n + j)
                if grid[i][j] == "\\":
                    union(parent, base, base + 3)
                    union(parent, base + 1, base + 2)
                elif grid[i][j] == "/":
                    union(parent, base, base + 1)
                    union(parent, base + 2, base + 3)
                else:
                    union(parent, base, base + 1)
                    union(parent, base + 1, base + 2)
                    union(parent, base + 2, base + 3)

                if j + 1 < n:
                    union(parent, base + 1, 4 * (i * n + j + 1) + 3)
                if i + 1 < n:
                    union(parent, base + 2, 4 * ((i + 1) * n + j))

        regions = set()
        for i in range(size):
            regions.add(find(parent, i))

        return len(regions)
