from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls_built = 0

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and isInfected[i][j] == 0:
                return 1
            if isInfected[i][j] == 1:
                isInfected[i][j] = -1
                infected_neighbours.append((i, j))
                return 0
            return 0

        def build_walls(region):
            walls = set()
            for i, j in region:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and isInfected[ni][nj] == 0:
                        walls.add((ni, nj))
            for i, j in walls:
                isInfected[i][j] = 1

        def spread_virus(region):
            new_region = []
            for i, j in region:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and isInfected[ni][nj] == 0:
                        new_region.append((ni, nj))
                        isInfected[ni][nj] = -1
                        walls_built += 1
            return new_region

        while True:
            regions = []
            visited = set()
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        region = []
                        infected_neighbours = [(i, j)]
                        walls_built += build_walls(infected_neighbours)
                        while infected_neighbours:
                            cell = infected_neighbours.pop()
                            visited.add(cell)
                            region.append(cell)
                            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                ni, nj = cell[0] + di, cell[1] + dj
                                dfs(ni, nj)
                        regions.append(region)

            if not regions:
                break

            regions.sort(key=len, reverse=True)
            quarantined_region = regions[0]
            walls_built -= len(quarantined_region)
            for region in regions[1:]:
                build_walls(region)
            isInfected = [row[:] for row in isInfected]

            new_regions = spread_virus(quarantined_region)
            for region in regions[1:]:
                new_regions += spread_virus(region)

            if not new_regions:
                break

        return walls_built
