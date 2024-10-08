from heapq import heappush, heappop

class Solution:
    
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = 0
        max_height = 0

        while heap:
            height, i, j = heappop(heap)
            max_height = max(max_height, height)
            
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, max_height - heightMap[x][y])
                    heappush(heap, (heightMap[x][y], x, y))
                    visited[x][y] = 1

        return result
