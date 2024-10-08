from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = [i for i in range(4*n*n)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            parent[root_x] = root_y

        for i in range(n):
            for j in range(n):
                idx = 4 * (i*n + j)
                if grid[i][j] == ' ':
                    union(idx, idx + 1)
                    union(idx + 1, idx + 2)
                    union(idx + 2, idx + 3)
                elif grid[i][j] == '/':
                    union(idx, idx + 3)
                    union(idx + 1, idx + 2)
                else:
                    union(idx, idx + 1)
                    union(idx + 2, idx + 3)

                # Union neighboring cells
                if i > 0:
                    union(idx, idx - 4*n + 2)
                if i < n - 1:
                    union(idx + 2, idx + 4*n)
                if j > 0:
                    union(idx + 3, idx - 4 + 1)
                if j < n - 1:
                    union(idx + 1, idx + 4 + 3)

        regions = set()
        for i in range(4*n*n):
            regions.add(find(i))

        return len(regions)
