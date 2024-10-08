class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        swim_time = 0
        seen = set()
        heap = [(grid[0][0], 0, 0)]  # (elevation, x, y)
        
        while heap:
            elevation, x, y = heapq.heappop(heap)
            swim_time = max(swim_time, elevation)
            if x == y == n - 1:
                return swim_time
            seen.add((x, y))
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen:
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))

        return -1
