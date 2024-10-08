from typing import List

class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        colors = [0] * n

        def dfs(node):
            if colors[node] != 0:
                return colors[node] == 1
            colors[node] = 2
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            colors[node] = 1
            return True

        return [i for i in range(n) if dfs(i)]

