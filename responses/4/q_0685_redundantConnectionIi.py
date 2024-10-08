from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {}
        candidates = []
        for u, v in edges:
            if v in parents:
                candidates.append([parents[v], v])
                candidates.append([u, v])
            else:
                parents[v] = u
        
        if not candidates:
            return self.find_cycle(edges)
        
        if len(candidates) == 2:
            return candidates[1]
        else:
            return candidates[0]
    
    def find_cycle(self, edges: List[List[int]]) -> List[int]:
        parents = list(range(len(edges) + 1))
        
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]
        
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return [u, v]
            parents[pv] = pu
        
        return []
