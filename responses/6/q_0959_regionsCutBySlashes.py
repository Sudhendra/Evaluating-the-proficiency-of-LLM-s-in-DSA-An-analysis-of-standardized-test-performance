from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = [i for i in range(4 * n * n)]

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
                base = 4 * (i * n + j)
                if grid[i][j] == "\\":
                    union(base, base + 1)
                    union(base + 2, base + 3)
                elif grid[i][j] == "/":
                    union(base, base + 3)
                    union(base + 1, base + 2)
                else:
                    union(base, base + 1)
                    union(base + 1, base + 2)
                    union(base + 2, base + 3)

                if j < n - 1:
                    union(base + 1, 4 * (i * n + j + 1) + 3)
                if i < n - 1:
                    union(base + 2, 4 * ((i + 1) * n + j))

        regions = set()
        for i in range(4 * n * n):
            regions.add(find(i))

        return len(regions)
