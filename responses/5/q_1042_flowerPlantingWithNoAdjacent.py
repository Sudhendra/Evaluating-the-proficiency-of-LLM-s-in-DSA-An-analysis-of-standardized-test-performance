from collections import defaultdict

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]) -> List[int]:
        graph = defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)

        colors = [0] * (n + 1)
        for i in range(1, n + 1):
            unavailable_colors = {colors[neighbor] for neighbor in graph[i]}
            for color in range(1, 5):
                if color not in unavailable_colors:
                    colors[i] = color
                    break

        return colors[1:]
