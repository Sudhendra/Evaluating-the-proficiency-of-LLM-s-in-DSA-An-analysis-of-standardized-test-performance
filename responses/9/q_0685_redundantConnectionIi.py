from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] * len(edges)
        def find(x):
            if parent[x] == 0:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return [x, y]
            parent[root_x] = root_y
        
        candidate1, candidate2, redundant = None, None, None
        # Check for a cycle
        for edge in edges:
            if parent[edge[1] - 1] == 0:
                parent[edge[1] - 1] = edge[0] - 1
            else:
                candidate1 = [parent[edge[1] - 1] + 1, edge[1]]
                candidate2 = edge
                redundant = edge
                edge[1] = 0
                
        parent = list(range(len(edges)))  # Reset parents
        # Check for a redundant edge among the remaining edges
        for edge in edges:
            if edge[1] == 0:
                continue
            if union(edge[0] - 1, edge[1] - 1):
                return candidate1 if candidate1 else edge
        
        return redundant
