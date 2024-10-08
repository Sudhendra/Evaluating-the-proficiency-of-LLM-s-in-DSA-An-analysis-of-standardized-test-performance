from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        
        import heapq
        visited = set()
        heap = []
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while heap:
            h, i, j = heapq.heappop(heap)
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    ans += max(0, h - heightMap[x][y])
                    heapq.heappush(heap, (max(h, heightMap[x][y]), x, y))
                    visited.add((x, y))
        
        return ans
