class Solution:
    def findRedundantConnection(self, edges: List[List[int]) -> List[int]:
        def find(parents, i):
            if parents[i] == -1:
                return i
            return find(parents, parents[i])
        
        def union(parents, x, y):
            parent_x = find(parents, x)
            parent_y = find(parents, y)
            if parent_x != parent_y:
                parents[parent_x] = parent_y
        
        n = len(edges)
        parents = [-1] * (n + 1)
        
        for edge in edges:
            x = find(parents, edge[0])
            y = find(parents, edge[1])
            
            if x == y:
                return edge
            else:
                union(parents, x, y)
        
        return []
