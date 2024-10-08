class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parents[root_x] = root_y

        n = len(grid)
        parents = [i for i in range(4 * n * n)]

        for i in range(n):
            for j in range(n):
                start = 4 * (i * n + j)
                if grid[i][j] == '/':
                    union(start, start + 1)
                    union(start + 2, start + 3)
                elif grid[i][j] == '\\':
                    union(start, start + 3)
                    union(start + 1, start + 2)
                else:
                    union(start, start + 1)
                    union(start, start + 2)
                    union(start, start + 3)

                if j + 1 < n:
                    union(start + 1, 4 * (i * n + j + 1) + 3)
                if i + 1 < n:
                    union(start + 2, 4 * ((i + 1) * n + j))

        regions = sum(parents[x] == x for x in range(4 * n * n))
        return regions
