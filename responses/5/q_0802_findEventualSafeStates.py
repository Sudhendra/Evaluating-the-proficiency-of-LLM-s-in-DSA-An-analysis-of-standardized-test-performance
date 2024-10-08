from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe_nodes = []

        color = [0] * n  # 0: not visited, 1: visiting, 2: visited

        def dfs(node):
            if color[node] > 0:
                return color[node] == 2

            color[node] = 1
            for neighbor in graph[node]:
                if color[neighbor] == 1 or (color[neighbor] == 0 and not dfs(neighbor)):
                    return False

            color[node] = 2
            return True
        
        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)

        return safe_nodes
