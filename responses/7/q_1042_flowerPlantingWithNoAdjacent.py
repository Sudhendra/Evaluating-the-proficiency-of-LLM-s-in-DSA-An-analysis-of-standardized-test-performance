class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for x, y in paths:
            graph[x - 1].append(y)
            graph[y - 1].append(x)

        result = [0] * n
        for i in range(n):
            neighbors_colors = set()
            for neighbor in graph[i]:
                neighbors_colors.add(result[neighbor - 1])
            for color in range(1, 5):
                if color not in neighbors_colors:
                    result[i] = color
                    break
        return result
