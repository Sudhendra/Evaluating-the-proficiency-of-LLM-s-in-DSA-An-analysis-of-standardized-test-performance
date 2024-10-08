from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        min_heap = [(grid[0][0], 0, 0)]
        max_elevation = grid[0][0]
        
        while min_heap:
            elevation, x, y = heapq.heappop(min_heap)
            max_elevation = max(max_elevation, elevation)
            
            if x == n - 1 and y == n - 1:
                return max_elevation
            
            seen.add((x, y))
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in seen:
                    heapq.heappush(min_heap, (grid[new_x][new_y], new_x, new_y))

        return -1
