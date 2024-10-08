from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, i):
            if parent[i] == -1:
                return i
            return find(parent, parent[i])

        n = len(edges)
        parent = [-1] * (n + 1)
        candidate1 = candidate2 = None
        cycle = None

        for u, v in edges:
            if parent[v] != -1:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
            else:
                parent[v] = u

                pu = find(parent, u)
                pv = find(parent, v)

                if pu == pv:
                    cycle = [u, v]
                else:
                    parent[pv] = pu

        if not candidate1:
            return cycle
        if not cycle:
            return candidate2
        return candidate1
