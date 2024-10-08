from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] * (len(edges) + 1)
        
        def find(x):
            if parent[x] == 0:
                return x
            return find(parent[x])
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return True
            parent[rootX] = rootY
            return False
        
        for edge in edges:
            if union(edge[0], edge[1]):
                return edge
        return []
