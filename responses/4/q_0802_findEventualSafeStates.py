from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n  # 0: not visited, 1: visiting, 2: visited and safe

        def is_safe(node):
            if color[node] > 0:
                return color[node] == 2
            color[node] = 1
            for neighbor in graph[node]:
                if color[neighbor] == 1 or not is_safe(neighbor):
                    return False
            color[node] = 2
            return True

        return [i for i in range(n) if is_safe(i)]
