from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        def find(node):
            if node not in parent:
                return node
            return find(parent[node])

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return False
            parent[root1] = root2
            return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
