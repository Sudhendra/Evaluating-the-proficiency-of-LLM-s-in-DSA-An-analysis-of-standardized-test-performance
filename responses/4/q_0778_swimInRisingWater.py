from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        
        while heap:
            time, x, y = heapq.heappop(heap)
            if x == y == n - 1:
                return time
            
            visited.add((x, y))
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited:
                    new_time = max(time, grid[new_x][new_y])
                    heapq.heappush(heap, (new_time, new_x, new_y))
