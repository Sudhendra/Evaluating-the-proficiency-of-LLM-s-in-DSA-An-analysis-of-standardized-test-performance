from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        colors = [0] * n
        for i in range(n):
            available_colors = [1, 2, 3, 4]
            for neighbor in graph[i]:
                if colors[neighbor] != 0 and colors[neighbor] in available_colors:
                    available_colors.remove(colors[neighbor])
            colors[i] = available_colors[0]

        return colors
