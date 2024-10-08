from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        def dfs(i, j, wall):
            if (i, j) in visited or isInfected[i][j] == 0:
                return 0
            visited.add((i, j))
            walls = 0
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < len(isInfected) and 0 <= y < len(isInfected[0]):
                    walls += dfs(x, y, wall)
            wall.append((i, j))
            return walls + 1

        def bfs(region):
            infected = set(region)
            frontier = set(region)
            to_infect = set()
            walls = 0
            while frontier:
                new_frontier = set()
                for i, j in frontier:
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if (x, y) in infected:
                            continue
                        if 0 <= x < len(isInfected) and 0 <= y < len(isInfected[0]):
                            if isInfected[x][y] == 1:
                                infected.add((x, y))
                                new_frontier.add((x, y))
                            else:
                                to_infect.add((x, y))
                                walls += 1
                frontier = new_frontier
            
            for i, j in to_infect:
                isInfected[i][j] = 1

            return walls

        walls = 0
        while True:
            visited = set()
            regions = []
            for i in range(len(isInfected)):
                for j in range(len(isInfected[0]):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        region = []
                        walls += dfs(i, j, region)
                        regions.append(region)

            if not regions:
                break

            regions.sort(key=lambda x: len(x), reverse=True)
            walls += bfs(regions[0])

        return walls
