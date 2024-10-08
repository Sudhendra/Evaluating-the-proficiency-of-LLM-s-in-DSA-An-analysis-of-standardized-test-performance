from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Kahn's algorithm for topological sorting
        n = len(graph)
        in_degree = [0] * n
        reverse_graph = [[] for _ in range(n)]

        for u, neighbors in enumerate(graph):
            in_degree[u] = len(neighbors)
            for v in neighbors:
                reverse_graph[v].append(u)

        queue = [u for u in range(n) if in_degree[u] == 0]
        result = []

        while queue:
            u = queue.pop(0)
            result.append(u)

            for v in reverse_graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        return sorted(result)
