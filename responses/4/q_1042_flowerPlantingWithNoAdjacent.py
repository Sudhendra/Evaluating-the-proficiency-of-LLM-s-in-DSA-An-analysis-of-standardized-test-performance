class Solution:
    
    def gardenNoAdj(self, n: int, paths: List[List[int]) -> List[int]:
        graph = {i: [] for i in range(1, n+1)}
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        
        flowers = [0] * (n + 1)
        
        for garden in range(1, n+1):
            neighboring_flowers = {flowers[neighbor] for neighbor in graph[garden]}
            for flower in range(1, 5):
                if flower not in neighboring_flowers:
                    flowers[garden] = flower
                    break
        
        return flowers[1:]
