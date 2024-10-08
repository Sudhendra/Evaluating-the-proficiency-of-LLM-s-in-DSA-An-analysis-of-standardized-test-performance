from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        keys = 0
        visited = set()
        start_i, start_j = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start_i, start_j = i, j
                if 'a' <= grid[i][j] <= 'f':
                    keys |= 1 << (ord(grid[i][j]) - ord('a'))
        
        queue = deque([(start_i, start_j, 0, 0)])
        while queue:
            i, j, collected_keys, steps = queue.popleft()
            if collected_keys == (1 << keys) - 1:
                return steps
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != '#':
                    if 'A' <= grid[ni][nj] <= 'F' and not (collected_keys >> (ord(grid[ni][nj]) - ord('A')) & 1):
                        continue
                    if 'a' <= grid[ni][nj] <= 'f':
                        new_collected_keys = collected_keys | 1 << (ord(grid[ni][nj]) - ord('a'))
                    else:
                        new_collected_keys = collected_keys
                    if (ni, nj, new_collected_keys) not in visited:
                        visited.add((ni, nj, new_collected_keys))
                        queue.append((ni, nj, new_collected_keys, steps + 1))
        
        return -1
