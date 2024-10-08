from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        min_heap = []

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0

        while min_heap:
            height, row, col = heapq.heappop(min_heap)

            for dx, dy in dirs:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n and not visited[new_row][new_col]:
                    ans += max(0, height - heightMap[new_row][new_col])
                    heapq.heappush(min_heap, (max(heightMap[new_row][new_col], height), new_row, new_col))
                    visited[new_row][new_col] = True

        return ans