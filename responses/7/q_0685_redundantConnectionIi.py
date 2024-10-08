from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        candidate1 = []
        candidate2 = []

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return [x, y]
            parent[root_y] = root_x
            return []

        for edge in edges:
            x, y = edge
            if parent[y] != y:
                candidate1 = [parent[y], y]
                candidate2 = edge
                edge[1] = 0
            else:
                parent[y] = x

        parent = list(range(len(edges) + 1))
        for edge in edges:
            x, y = edge
            if y == 0:
                continue
            result = union(x, y)
            if result:
                return result

        return candidate2

# Sample test cases
edges1 = [[1,2],[1,3],[2,3]]
edges2 = [[1,2],[2,3],[3,4],[4,1],[1,5]]

sol = Solution()
print(sol.findRedundantDirectedConnection(edges1))  # Output: [2,3]
print(sol.findRedundantDirectedConnection(edges2))  # Output: [4,1]
