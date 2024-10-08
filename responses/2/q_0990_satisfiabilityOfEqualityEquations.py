from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = {}
        
        def find(x):
            if x not in graph:
                graph[x] = x
                return x
            if graph[x] != x:
                graph[x] = find(graph[x])
            return graph[x]
        
        def union(x, y):
            graph[find(x)] = find(y)
        
        for eq in equations:
            if eq[1] == "=":
                x, y = eq[0], eq[3]
                union(x, y)
        
        for eq in equations:
            if eq[1] == "!":
                x, y = eq[0], eq[3]
                if find(x) == find(y):
                    return False
                
        return True
