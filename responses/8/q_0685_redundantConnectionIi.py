from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return [node1, node2]
            if ranks[root1] > ranks[root2]:
                parents[root2] = root1
            elif ranks[root1] < ranks[root2]:
                parents[root1] = root2
            else:
                parents[root2] = root1
                ranks[root1] += 1
            return None

        n = len(edges)
        parents = {i + 1: i + 1 for i in range(n)}
        ranks = {i + 1: 0 for i in range(n)}
        cycle_edge = None
        two_parents_edge = None
        for edge in edges:
            u, v = edge
            if parents[v] != v:
                two_parents_edge = edge
            else:
                parents[v] = u
                cycle_edge_candidate = union(u, v)
                if cycle_edge_candidate:
                    cycle_edge = cycle_edge_candidate
        if not cycle_edge:
            return two_parents_edge
        if not two_parents_edge:
            return cycle_edge
        for edge in reversed(edges):
            if edge == two_parents_edge:
                return edge
