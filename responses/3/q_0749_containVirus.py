from typing import List

class Solution:

    def containVirus(self, isInfected: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and isInfected[i][j] == 0:
                uninfected.add((i, j))
                return area[i][j]
            return 0

        def dfs_contaminated(i, j, infected_region):
            if (i, j) in infected_region:
                return 0
            infected_region.add((i, j))
            total_contamination = 0
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and isInfected[x][y] == 1:
                    total_contamination += dfs_contaminated(x, y, infected_region)
            return total_contamination

        m, n = len(isInfected), len(isInfected[0])
        walls = 0

        while True:
            regions = []
            area = [[0] * n for _ in range(m)]
            uninfected = set()
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and area[i][j] == 0:
                        infected_region = set()
                        contamination = dfs_contaminated(i, j, infected_region)
                        if contamination > 0:
                            regions.append((len(infected_region), infected_region))
            if not regions:
                break

            regions.sort(reverse=True)
            walls_to_build = set()
            for _, region in regions:
                for i, j in region:
                    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if 0 <= x < m and 0 <= y < n and isInfected[x][y] == 0:
                            walls_to_build.add((x, y))

            walls += len(walls_to_build)
            for x, y in walls_to_build:
                isInfected[x][y] = -1

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == -1:
                        isInfected[i][j] = 1
                    if isInfected[i][j] == 1:
                        area[i][j] = dfs(i, j)

        return walls
