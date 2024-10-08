from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        
        pq = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        time = 0
        
        while pq:
            elevation, x, y = heapq.heappop(pq)
            time = max(time, elevation)
            
            if x == n - 1 and y == n - 1:
                return time
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(pq, (grid[nx][ny], nx, ny))
                    visited[nx][ny] = True
        
        return -1
