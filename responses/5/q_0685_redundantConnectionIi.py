from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, i):
            if parent[i] == -1:
                return i
            return find(parent, parent[i])

        def union(parent, x, y):
            x_set = find(parent, x)
            y_set = find(parent, y)
            if x_set != y_set:
                parent[y_set] = x_set

        n = len(edges)
        parent = [-1] * (n + 1)
        candidate1 = None
        candidate2 = None
        cycle_edge = None

        for edge in edges:
            u = edge[0]
            v = edge[1]
            if parent[v] == -1:
                parent[v] = u
            else:
                candidate1 = [parent[v], v]
                candidate2 = edge

                # Remove the last edge that creates a cycle in the graph
                cycle_edge = edge
                break

        if not cycle_edge:
            return candidate2

        for edge in edges:
            if edge == cycle_edge:
                continue
            if find(parent, edge[0]) == find(parent, edge[1]):
                return candidate1

        return cycle_edge
