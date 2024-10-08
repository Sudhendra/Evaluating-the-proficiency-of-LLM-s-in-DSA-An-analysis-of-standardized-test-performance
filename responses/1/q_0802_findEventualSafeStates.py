class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2
        n = len(graph)
        color = [WHITE] * n

        def is_safe(node):
            if color[node] != WHITE:
                return color[node] == BLACK
            color[node] = GRAY
            for neighbor in graph[node]:
                if color[neighbor] == BLACK or is_safe(neighbor):
                    continue
                return False
            color[node] = BLACK
            return True

        return [node for node in range(n) if is_safe(node)]