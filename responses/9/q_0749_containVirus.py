from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < len(isInfected) and 0 <= j < len(isInfected[0]) and isInfected[i][j] == 0:
                uninfected_cells.add((i, j))
            elif 0 <= i < len(isInfected) and 0 <= j < len(isInfected[0]) and isInfected[i][j] == 1 and (i, j) not in infected_cells:
                infected_cells.add((i, j))
                walls_to_build.add((i, j))
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    dfs(x, y)

        def expand_virus(region):
            perimeter = set()
            for i, j in region:
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < len(isInfected) and 0 <= y < len(isInfected[0]) and (x, y) not in region:
                        perimeter.add((x, y))
            return perimeter

        def build_walls(region):
            nonlocal walls_built
            for i, j in region:
                isInfected[i][j] = -1
            walls_built += len(region)

        def quarantine(region):
            global walls_built
            walls_to_build.clear()
            for i, j in region:
                dfs(i, j)
            build_walls(walls_to_build)
            next_regions = []
            infecting_perimeter = set()
            for i, j in region:
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < len(isInfected) and 0 <= y < len(isInfected[0]) and isInfected[x][y] == 0:
                        infecting_perimeter.add((x, y))
            next_region = expand_virus(infecting_perimeter)
            if next_region:
                next_regions.append(next_region)

            for r in next_regions:
                quarantine(r)

        walls_built = 0
        while True:
            regions = []
            for i in range(len(isInfected)):
                for j in range(len(isInfected[0])):
                    if isInfected[i][j] == 1:
                        infected_cells = set()
                        uninfected_cells = set()
                        walls_to_build = set()
                        dfs(i, j)
                        regions.append(infected_cells)

            if not regions:
                break

            max_region_idx = max(range(len(regions)), key=lambda x: len(regions[x]))
            quarantine(regions[max_region_idx])
        
        return walls_built
