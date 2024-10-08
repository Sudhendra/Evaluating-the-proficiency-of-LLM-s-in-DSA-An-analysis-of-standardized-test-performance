from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)

            if root_x == root_y:
                return

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        def is_similar(a, b):
            num_diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    num_diff += 1
                if num_diff > 2:
                    return False
            return True

        n = len(strs)
        parent = [i for i in range(n)]
        rank = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if is_similar(strs[i], strs[j]):
                    union(parent, rank, i, j)

        groups = set()
        for i in range(n):
            groups.add(find(parent, i))

        return len(groups)