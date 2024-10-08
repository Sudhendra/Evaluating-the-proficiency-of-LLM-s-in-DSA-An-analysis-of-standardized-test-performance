from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        pq = [(grid[0][0], 0, 0)]
        
        while pq:
            time, x, y = heapq.heappop(pq)
            max_time = max(time, grid[x][y])
            
            if x == n - 1 and y == n - 1:
                return max_time
            
            visited.add((x, y))
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    heapq.heappush(pq, (max_time, nx, ny))
                    visited.add((nx, ny))

        return -1
