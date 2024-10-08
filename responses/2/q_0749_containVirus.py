from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls = 0
        
        def check_neighbors(row, col, visited):
            if row < 0 or row >= m or col < 0 or col >= n or isInfected[row][col] == 2 or (row, col) in visited:
                return
            if isInfected[row][col] == 0:
                isInfected[row][col] = 2
                visited.add((row, col))
                return
            visited.add((row, col))
            check_neighbors(row+1, col, visited)
            check_neighbors(row-1, col, visited)
            check_neighbors(row, col+1, visited)
            check_neighbors(row, col-1, visited)
        
        while True:
            regions = {}  # key: region id, value: set of coordinates
            regions_to_wall = {}  # key: region id, value: set of coordinates of walls to build
            total_uninfected_neighbors = {}
            region_id = 0
            
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        if (i, j) not in regions and (i, j) not in total_uninfected_neighbors:
                            infected_cells = set()
                            uninfected_neighbors = set()
                            check_neighbors(i, j, infected_cells)
                            for r, c in infected_cells:
                                for x, y in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                                    if 0 <= x < m and 0 <= y < n and isInfected[x][y] == 0:
                                        uninfected_neighbors.add((x, y))
                            total_uninfected_neighbors[(i, j)] = uninfected_neighbors
                            regions[region_id] = infected_cells
                            region_id += 1
            
            if not regions:
                break
            
            largest_region_id = max(regions, key=lambda x: len(regions[x]))
            walls_to_build = total_uninfected_neighbors.pop(largest_region_id)
            walls += len(walls_to_build)
            
            for r_id, region in regions.items():
                if r_id == largest_region_id:
                    for r, c in region:
                        isInfected[r][c] = -1
                else:
                    for r, c in region:
                        isInfected[r][c] = 1
                        for x, y in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                            if 0 <= x < m and 0 <= y < n and (x, y) in walls_to_build:
                                isInfected[x][y] = 1
                        
        return walls
