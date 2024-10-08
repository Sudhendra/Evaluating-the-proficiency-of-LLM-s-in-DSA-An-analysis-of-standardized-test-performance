from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        walls = 0
        
        def dfs(i, j, region, perimeter):
            if (i, j) in region:
                return
            if isInfected[i][j] == 0:
                perimeter.add((i, j))
                return
            region.add((i, j))
            for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= ni < len(isInfected) and 0 <= nj < len(isInfected[0]):
                    dfs(ni, nj, region, perimeter)
        
        def build_walls(region):
            infected_border = set()
            for i, j in region:
                for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0 <= ni < len(isInfected) and 0 <= nj < len(isInfected[0]) and (ni, nj) not in region:
                        infected_border.add((ni, nj))
            for i, j in infected_border:
                isInfected[i][j] = 1
            return len(infected_border)
        
        while True:
            regions = []
            perimeters = []
            visited = set()
            max_region = set()
            max_perimeter = set()
            
            for i in range(len(isInfected)):
                for j in range(len(isInfected[0]):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        region = set()
                        perimeter = set()
                        dfs(i, j, region, perimeter)
                        regions.append(region)
                        perimeters.append(perimeter)
                        visited |= region
                        
                        if len(region) > len(max_region):
                            max_region = region
                            max_perimeter = perimeter
            
            if not regions:
                break
            
            walls += build_walls(max_region)
            
            for i in range(len(regions)):
                if regions[i] != max_region:
                    for i, j in perimeters[i]:
                        isInfected[i][j] = 1
        
        return walls
