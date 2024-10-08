from collections import defaultdict

class Solution:

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        colors = [0] * (n + 1)
        
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
    
        def dfs(person, color):
            colors[person] = color
            for neighbor in graph[person]:
                if colors[neighbor] == color:
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    return False
            return True
    
        for person in range(1, n + 1):
            if colors[person] == 0 and not dfs(person, 1):
                return False
        
        return True
