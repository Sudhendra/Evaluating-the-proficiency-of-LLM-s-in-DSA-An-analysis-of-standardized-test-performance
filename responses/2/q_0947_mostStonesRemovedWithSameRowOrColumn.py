from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = {}
        for i, (x, y) in enumerate(stones):
            if x not in graph:
                graph[x] = []
            graph[x].append(i + 1000)
            if y not in graph:
                graph[y] = []
            graph[y].append(i)

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    dfs(neighbor)

        visited = set()
        components = 0
        for i, (x, y) in enumerate(stones):
            if i not in visited:
                dfs(i)
                components += 1

        return len(stones) - components
