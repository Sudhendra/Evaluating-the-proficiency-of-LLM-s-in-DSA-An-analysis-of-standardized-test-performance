from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                parent[root1] = root2

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        n = len(stones)
        parent = {i: i for i in range(n)}
        for i in range(n):
            for j in range(i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)

        return n - len({find(i) for i in parent})
