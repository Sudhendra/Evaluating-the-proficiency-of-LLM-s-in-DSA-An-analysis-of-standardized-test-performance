class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def is_stable(x, y):
            if x == 0:
                return True
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) in stable_bricks:
                    return True
            return False

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] != 1 or (x, y) in visited:
                return 0
            visited.add((x, y))
            return 1 + sum(dfs(x+dx, y+dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)])

        def connected_to_top():
            return any(grid[0][j] for j in range(n))

        def count_stable_bricks():
            return sum(is_stable(0, j) for j in range(n))

        def update_connected(x, y):
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    if is_stable(nx, ny):
                        uf.union(x*n+y, nx*n+ny)

        m, n = len(grid), len(grid[0])
        uf = UnionFind(m*n + 1)  # 1 extra for the virtual top node
        for i, j in hits:
            grid[i][j] -= 1

        for j in range(n):
            if grid[0][j] == 1:
                uf.union(j, m*n)

        for i in range(1, m):
            for j in range(n):
                if grid[i][j] == 1:
                    if grid[i-1][j] == 1:
                        uf.union(i*n+j, (i-1)*n+j)
                    if j > 0 and grid[i][j-1] == 1:
                        uf.union(i*n+j, i*n+j-1)

        ans = []
        visited = set()
        stable_bricks = {(0, j) for j in range(n) if grid[0][j] == 1}

        for i, j in reversed(hits):
            if grid[i][j] == 0:
                ans.append(0)
                continue
            origin = count_stable_bricks()
            grid[i][j] = 1
            if i == 0 or any((ni, nj) in stable_bricks for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]):
                update_connected(i, j)
                if connected_to_top():
                    for j in range(n):
                        if grid[0][j] == 1:
                            uf.union(j, m*n)

                cur = count_stable_bricks()
                stable_bricks.add((i, j))
                ans.append(max(0, cur - origin - 1))
            else:
                ans.append(0)

        return ans
