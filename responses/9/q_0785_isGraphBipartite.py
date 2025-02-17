from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    return False
            return True

        for i in range(n):
            if colors[i] == 0 and not dfs(i, 1):
                return False
        return True
