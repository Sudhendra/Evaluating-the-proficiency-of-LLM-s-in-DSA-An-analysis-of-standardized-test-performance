class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        colors = [0] * n
        for i in range(n):
            neighbor_colors = {colors[j] for j in graph[i]}
            for c in range(1, 5):
                if c not in neighbor_colors:
                    colors[i] = c
                    break

        return colors

# Additional solution using different approach
    def gardenNoAdj_alternative(self, n: int, paths: List[List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        flowers = [0] * n
        for i in range(n):
            used_colors = {flowers[j] for j in graph[i]}
            available_colors = {1, 2, 3, 4} - used_colors
            flowers[i] = available_colors.pop()

        return flowers
