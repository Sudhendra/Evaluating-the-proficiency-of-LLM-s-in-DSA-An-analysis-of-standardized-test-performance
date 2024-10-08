from typing import List
from collections import deque

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        walls_built = 0

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and isInfected[i][j] == 0:
                infected_regions.add((i, j))
            elif 0 <= i < m and 0 <= j < n and isInfected[i][j] == 1 and (i, j) not in visited:
                visited.add((i, j))
                infected_cells.add((i, j))
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    dfs(ni, nj)

        def get_regions_to_quarantine():
            regions_to_quarantine = []
            max_uninfected_cells = -1
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        infected_cells.clear()
                        visited_cells = set()
                        dfs(i, j)
                        if len(infected_cells) > max_uninfected_cells:
                            max_uninfected_cells = len(infected_cells)
                            regions_to_quarantine.clear()
                            regions_to_quarantine.append(list(infected_regions))
                        infected_regions.clear()
            return regions_to_quarantine

        def build_walls(regions):
            for region in regions:
                for i, j in region:
                    isInfected[i][j] = -1
                for i, j in region:
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and isInfected[ni][nj] == 0:
                            walls_built += 1

        while True:
            infected_regions = set()
            infected_cells = set()
            visited = set()
            regions_to_quarantine = get_regions_to_quarantine()
            if not regions_to_quarantine:
                break
            build_walls(regions_to_quarantine)

        return walls_built
