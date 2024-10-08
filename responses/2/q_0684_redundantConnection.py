from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]) -> List[int]:
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)

            if x_root == y_root:
                return False

            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

            return True

        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        for edge in edges:
            if not union(parent, rank, edge[0], edge[1]):
                return edge
        return []
