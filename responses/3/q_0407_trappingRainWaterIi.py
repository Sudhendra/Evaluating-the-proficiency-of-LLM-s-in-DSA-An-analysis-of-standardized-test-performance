from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        trapped_water = 0
        max_height = float('-inf')
        visited = set()
        min_heap = []
        
        # Adding border cells to the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heappush(min_heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
        
        while min_heap:
            height, i, j = heappop(min_heap)
            max_height = max(max_height, height)
            
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    if heightMap[ni][nj] < max_height:
                        trapped_water += max_height - heightMap[ni][nj]
                    heappush(min_heap, (heightMap[ni][nj], ni, nj))
                    visited.add((ni, nj))
        
        return trapped_water
