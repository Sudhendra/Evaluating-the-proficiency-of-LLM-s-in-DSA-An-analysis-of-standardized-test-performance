from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        def dfs(row, col):
            if 0 <= row < m and 0 <= col < n and isInfected[row][col] == 0:
                regions[-1].add((row, col))
                walls[-1] += 1
                wall_set.add((row, col))
                return True
            return False

        def expand_virus(row, col):
            if 0 <= row < m and 0 <= col < n and isInfected[row][col] == 0 and (row, col) not in wall_set:
                isInfected[row][col] = 1
                for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                    expand_virus(r, c)

        def build_walls(region):
            walls_built = 0
            for row, col in region:
                for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                    if 0 <= r < m and 0 <= c < n and isInfected[r][c] == 0 and (r, c) not in wall_set:
                        walls_built += 1
            return walls_built

        result = 0
        m, n = len(isInfected), len(isInfected[0])
        while True:
            regions = []
            walls = []
            virus_regions = []
            wall_set = set()

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        if (i, j) not in wall_set:
                            region = set()
                            walls.append(0)
                            regions.append(region)
                            virus_regions.append(region)
                            dfs(i, j)
            
            if not regions:
                break

            target_region_idx = walls.index(max(walls))
            result += build_walls(virus_regions[target_region_idx])
            for i, region in enumerate(virus_regions):
                if i == target_region_idx:
                    for row, col in region:
                        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                            expand_virus(r, c)

        return result
