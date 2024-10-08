from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        colors = [0] * n
        
        def is_safe(node, color):
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False
            return True
        
        def assign_color(node):
            for color in range(1, 5):
                if is_safe(node, color):
                    colors[node] = color
                    break
        
        for node in range(n):
            assign_color(node)
        
        return colors