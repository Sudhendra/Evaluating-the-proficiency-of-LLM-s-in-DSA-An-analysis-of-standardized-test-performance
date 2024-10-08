class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        trapped_water = 0
        pq = []
        visited = set()

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    visited.add((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while pq:
            h, i, j = heapq.heappop(pq)

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    nh = max(h, heightMap[ni][nj])
                    trapped_water += max(0, nh - heightMap[ni][nj])
                    heapq.heappush(pq, (nh, ni, nj))
                    visited.add((ni, nj))

        return trapped_water
