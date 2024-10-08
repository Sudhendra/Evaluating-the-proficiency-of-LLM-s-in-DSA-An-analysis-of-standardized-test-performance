from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = {}
        rows = {}
        cols = {}
        
        def dfs(x, y):
            if (x, y) in graph:
                return
            graph[(x, y)] = []
            for i in rows[x]:
                graph[(x, y)].append((x, i))
                dfs(x, i)
            for j in cols[y]:
                graph[(x, y)].append((j, y))
                dfs(j, y)
        
        for x, y in stones:
            if x not in rows:
                rows[x] = []
            if y not in cols:
                cols[y] = []
            rows[x].append(y)
            cols[y].append(x)
        
        islands = 0
        for x, y in stones:
            if (x, y) not in graph:
                islands += 1
                dfs(x, y)
        
        return len(stones) - islands
