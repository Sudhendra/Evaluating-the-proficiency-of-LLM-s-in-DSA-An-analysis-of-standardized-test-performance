from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(a, b):
            if a == b:
                return True
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 2

        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x == root_y:
                return
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        n = len(strs)
        parent = list(range(n))
        rank = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if similar(strs[i], strs[j]):
                    union(parent, rank, i, j)

        groups = set()
        for i in range(n):
            groups.add(find(parent, i))

        return len(groups)
