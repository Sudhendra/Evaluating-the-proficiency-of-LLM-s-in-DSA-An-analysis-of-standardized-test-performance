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
            parent[find(x)] = find(y)
        
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
                
                if j + 1 < n:
                    union(idx + 1, 4 * (i * n + j + 1) + 3)
                    
                if i + 1 < n:
                    union(idx + 2, 4 * ((i + 1) * n + j))
        
        regions = set()
        for i in range(4 * n * n):
            regions.add(find(i))
        
        return len(regions)
