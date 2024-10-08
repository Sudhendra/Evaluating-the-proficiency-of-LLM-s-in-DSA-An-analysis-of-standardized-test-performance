from collections import defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parent = [-1]  # Parent array for union-find
        rank = [0]  # Rank array for union-find
        area = defaultdict(int)  # Dictionary to store island area

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                    area[root_x] += area[root_y]
                else:
                    parent[root_x] = root_y
                    area[root_y] += area[root_x]
                    if rank[root_x] == rank[root_y]:
                        rank[root_y] += 1

        def get_area(i, j, idx):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1 and idx not in visited:
                visited.add(idx)
                return 1 + sum([get_area(x, y, idx) for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]])
            return 0

        islands = set()
        max_area = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in islands:
                    visited = set()
                    curr_area = get_area(i, j, (i, j))
                    max_area = max(max_area, curr_area)
                    area[(i, j)] = curr_area
                    islands.add((i, j))

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_areas = set()
                    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            neighbor_areas.add(find(x*n + y))
                    
                    total_area = 1 + sum([area[root] for root in neighbor_areas])
                    max_area = max(max_area, total_area)

        return max_area
