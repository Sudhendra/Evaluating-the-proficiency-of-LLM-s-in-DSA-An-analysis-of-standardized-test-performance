from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        minHeap = []
        result = 0

        # Add all border cells to the minHeap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        # Perform BFS to process cells by height
        while minHeap:
            height, row, col = heapq.heappop(minHeap)
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                newRow, newCol = row + dx, col + dy
                if 0 <= newRow < m and 0 <= newCol < n and not visited[newRow][newCol]:
                    newHeight = max(height, heightMap[newRow][newCol])
                    result += max(0, newHeight - heightMap[newRow][newCol])
                    heapq.heappush(minHeap, (newHeight, newRow, newCol))
                    visited[newRow][newCol] = True
        
        return result
