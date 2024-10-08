from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        keys = 0
        start_row, start_col = -1, -1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    start_row, start_col = r, c
                elif 'a' <= grid[r][c] <= 'f':
                    keys = max(keys, ord(grid[r][c]) - ord('a') + 1)
        
        def bfs(sr, sc):
            visited = set()
            queue = deque([(sr, sc, 0, '')])
            while queue:
                r, c, steps, collected = queue.popleft()
                if len(collected) == keys:
                    return steps
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                        if 'A' <= grid[nr][nc] <= 'F' and grid[nr][nc].lower() not in collected:
                            continue
                        if grid[nr][nc] in collected or (grid[nr][nc].islower() and grid[nr][nc] not in collected):
                            new_collected = collected
                        else:
                            new_collected = collected + grid[nr][nc]
                        if (nr, nc, new_collected) not in visited:
                            visited.add((nr, nc, new_collected))
                            queue.append((nr, nc, steps + 1, new_collected))
            
            return -1
        
        return bfs(start_row, start_col)
