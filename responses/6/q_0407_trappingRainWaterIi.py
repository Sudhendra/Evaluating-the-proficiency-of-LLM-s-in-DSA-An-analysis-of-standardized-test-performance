from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        
        # Push the boundary into the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
        
        while heap:
            h, i, j = heappop(heap)
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    res += max(0, h - heightMap[x][y])
                    heappush(heap, (max(h, heightMap[x][y]), x, y))
                    visited.add((x, y))
        
        return res
