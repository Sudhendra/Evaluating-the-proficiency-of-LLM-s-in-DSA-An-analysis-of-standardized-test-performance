class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]) -> List[int]:
        def find(parents, x):
            if parents[x] != x:
                parents[x] = find(parents, parents[x])
            return parents[x]
        
        n = len(edges)
        parents = list(range(n + 1))
        candidate1, candidate2, to_node = None, None, None
        
        for edge in edges:
            u, v = edge
            if parents[v] != v:
                candidate1 = [parents[v], v]
                candidate2 = edge
            else:
                parents[v] = u
        
        for i in range(1, n + 1):
            parents[i] = i
        
        for edge in edges:
            if edge == candidate2:
                continue
            u, v = edge
            parent_u, parent_v = find(parents, u), find(parents, v)
            if parent_u == parent_v:
                return candidate1 if candidate1 else edge
            else:
                parents[parent_v] = parent_u
        
        return candidate2