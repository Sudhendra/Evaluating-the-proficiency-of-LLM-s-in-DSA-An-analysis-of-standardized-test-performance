from heapq import heappush, heappop

class Solution:
    
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        heap = []
        res = 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        while heap:
            height, x, y = heappop(heap)
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    res += max(0, height - heightMap[nx][ny])
                    heappush(heap, (max(heightMap[nx][ny], height), nx, ny))
                    visited[nx][ny] = True
        
        return res
