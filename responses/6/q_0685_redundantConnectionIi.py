from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find_parent(parents, i):
            if parents[i] == -1:
                return i
            return find_parent(parents, parents[i])

        def union(parents, x, y):
            x_parent = find_parent(parents, x)
            y_parent = find_parent(parents, y)
            if x_parent == y_parent:
                return True
            parents[x_parent] = y_parent
            return False

        def detect_cycle_and_determine_candidate(edges, n):
            parents = [-1] * (n + 1)
            candidate = None
            cycle_edge = None
            for edge in edges:
                u, v = edge
                if parents[v] == -1:
                    parents[v] = u
                else:
                    candidate = edge
                if find_parent(parents, u) == find_parent(parents, v):
                    cycle_edge = edge
                    if not candidate:
                        return cycle_edge
            return candidate if candidate else cycle_edge

        n = len(edges)
        return detect_cycle_and_determine_candidate(edges, n)
