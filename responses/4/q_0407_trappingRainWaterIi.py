from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        max_heap = []
        total_volume = 0
        
        # Push the border into the heap and mark them as visited
        for i in range(m):
            heappush(max_heap, (heightMap[i][0], i, 0))
            heappush(max_heap, (heightMap[i][n-1], i, n-1))
            visited[i][0] = True
            visited[i][n-1] = True
        for j in range(1, n-1):
            heappush(max_heap, (heightMap[0][j], 0, j))
            heappush(max_heap, (heightMap[m-1][j], m-1, j))
            visited[0][j] = True
            visited[m-1][j] = True
        
        while max_heap:
            h, i, j = heappop(max_heap)
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    total_volume += max(0, h - heightMap[x][y])
                    heappush(max_heap, (max(h, heightMap[x][y]), x, y))
                    visited[x][y] = True
        
        return total_volume
