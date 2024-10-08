from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)
        
        flowers = [0] * n
        for i in range(n):
            neighbors = set(flowers[j] for j in graph[i])
            for color in range(1, 5):
                if color not in neighbors:
                    flowers[i] = color
                    break
        
        return flowers
