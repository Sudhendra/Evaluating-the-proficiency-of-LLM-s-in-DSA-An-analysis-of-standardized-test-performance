from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, i, j):
            root_i = find(parent, i)
            root_j = find(parent, j)
            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                else:
                    parent[root_i] = root_j
                    rank[root_j] += 1

        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)
        
        for edge in edges:
            node1, node2 = edge
            if find(parent, node1) == find(parent, node2):
                return edge
            union(parent, rank, node1, node2)
