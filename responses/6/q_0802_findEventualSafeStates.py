from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0] * n
        safe_nodes = []

        def is_safe(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1
            for next_node in graph[node]:
                if not is_safe(next_node):
                    return False

            visited[node] = 2
            return True

        for i in range(n):
            if is_safe(i):
                safe_nodes.append(i)

        return safe_nodes
