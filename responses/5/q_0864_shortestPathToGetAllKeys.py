from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        keys = 0
        visited = set()
        queue = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    queue.append((i, j, 0))
                    visited.add((i, j, 0))
                if grid[i][j].islower():
                    keys |= 1 << (ord(grid[i][j]) - ord('a'))

        step = 0
        while queue:
            new_queue = []
            
            for i, j, key in queue:
                if key == keys:
                    return step
                
                for x, y in dirs:
                    ni, nj = i + x, j + y
                    nkey = key
                    
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != '#':
                        if grid[ni][nj].isupper() and not (key & (1 << (ord(grid[ni][nj]) - ord('A'))):
                            continue
                        if grid[ni][nj].islower():
                            nkey |= 1 << (ord(grid[ni][nj]) - ord('a'))
                        
                        if (ni, nj, nkey) not in visited:
                            new_queue.append((ni, nj, nkey))
                            visited.add((ni, nj, nkey))
            
            queue = new_queue
            step += 1
        
        return -1
