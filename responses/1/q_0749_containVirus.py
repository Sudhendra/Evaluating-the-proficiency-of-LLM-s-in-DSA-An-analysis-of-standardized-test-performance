from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and not visited[i][j] and isInfected[i][j] == 1:
                visited[i][j] = True
                region.append((i, j))
                for x,y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    dfs(x, y)
        
        def get_neighbours(i, j):
            return [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
        
        def build_walls(region):
            walls_built = 0
            for i, j in region:
                for x, y in get_neighbours(i, j):
                    if 0 <= x < m and 0 <= y < n and isInfected[x][y] == 0:
                        walls_built += 1
                        isInfected[x][y] = -1
            return walls_built
        
        def spread_virus(region):
            for i, j in region:
                for x, y in get_neighbours(i, j):
                    if 0 <= x < m and 0 <= y < n and isInfected[x][y] == 0:
                        isInfected[x][y] = 1
        
        def find_most_threatened():
            max_threatened = 0
            most_threatened_region = []
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        region.clear()
                        dfs(i, j)
                        if len(region) > max_threatened:
                            max_threatened = len(region)
                            most_threatened_region = region[:]
            return most_threatened_region
        
        m, n = len(isInfected), len(isInfected[0])
        walls_required = 0
        
        while True:
            visited = [[False for _ in range(n)] for _ in range(m)]
            region = []
            most_threatened_region = find_most_threatened()
            if not most_threatened_region:
                break
            walls_required += build_walls(most_threatened_region)
            spread_virus(most_threatened_region)
        
        return walls_required
