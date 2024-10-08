from collections import defaultdict

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]) -> List[int]:
        graph = defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        
        result = [0] * n
        for i in range(1, n+1):
            neighbor_colors = set()
            for neighbor in graph[i]:
                neighbor_colors.add(result[neighbor-1])
            for color in range(1, 5):
                if color not in neighbor_colors:
                    result[i-1] = color
                    break
        return result
