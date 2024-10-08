class Solution:
    def findRedundantConnection(self, edges: List[List[int]) -> List[int]:
        def find(parent, i):
            if parent[i] == -1:
                return i
            return find(parent, parent[i])

        def union(parent, x, y):
            x_set = find(parent, x)
            y_set = find(parent, y)
            if x_set != y_set:
                parent[x_set] = y_set

        n = len(edges)
        parent = [-1] * (n + 1)

        for edge in edges:
            x = find(parent, edge[0])
            y = find(parent, edge[1])
            if x == y:
                return edge
            union(parent, x, y)
