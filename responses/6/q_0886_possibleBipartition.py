from collections import defaultdict

class Solution:
    
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = {}
        
        def dfs(node, c):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c^1) for nei in graph[node])
        
        return all(dfs(node, 0) for node in range(1, n+1) if node not in color)
