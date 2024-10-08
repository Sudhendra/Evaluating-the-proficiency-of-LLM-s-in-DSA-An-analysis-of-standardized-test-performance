from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.parent[root_x] = root_y
        return True

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = DSU(4 * n * n)

        for r in range(n):
            for c in range(n):
                base = 4 * (r * n + c)
                if grid[r][c] in "/ ":
                    dsu.union(base, base + 1)
                    dsu.union(base + 2, base + 3)
                if grid[r][c] in "\ ":
                    dsu.union(base, base + 3)
                    dsu.union(base + 1, base + 2)
                
                if r > 0:
                    dsu.union(base, base - 4 * n + 2)
                if r < n - 1:
                    dsu.union(base + 2, base + 4 * n)
                    
                if c > 0:
                    dsu.union(base + 3, base - 4 + 1)
                if c < n - 1:
                    dsu.union(base + 1, base + 4 + 3)
        
        return sum(dsu.find(i) == i for i in range(4 * n * n))
