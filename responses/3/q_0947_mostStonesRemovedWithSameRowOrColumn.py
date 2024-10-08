from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(set)
        cols = defaultdict(set)
        islands = 0

        def dfs(x, y):
            rows[x].remove(y)
            cols[y].remove(x)
            for neighbor in rows[x] | cols[y]:
                if (neighbor, y) not in visited:
                    visited.add((neighbor, y))
                    dfs(neighbor, y)
                if (x, neighbor) not in visited:
                    visited.add((x, neighbor))
                    dfs(x, neighbor)

        for x, y in stones:
            if y not in rows[x]:
                islands += 1
                visited = set()
                dfs(x, y)

        return len(stones) - islands
