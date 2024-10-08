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
                idx = 4 * (i * n + j)
                if grid[i][j] == "/":
                    union(idx, idx + 3)
                    union(idx + 1, idx + 2)
                elif grid[i][j] == "\\":
                    union(idx, idx + 1)
                    union(idx + 2, idx + 3)
                else:
                    union(idx, idx + 1)
                    union(idx + 1, idx + 2)
                    union(idx + 2, idx + 3)

                if i < n - 1:
                    union(idx + 2, idx + 4 * n)
                if j < n - 1:
                    union(idx + 1, idx + 4 + 3)

        regions = set()
        for i in range(4 * n * n):
            regions.add(find(i))

        return len(regions)
