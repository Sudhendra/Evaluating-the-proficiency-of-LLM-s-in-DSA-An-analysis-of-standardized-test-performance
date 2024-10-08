from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find_parent(parent, i):
            if parent[i] == i:
                return i
            return find_parent(parent, parent[i])

        def union(parent, rank, x, y):
            x_root = find_parent(parent, x)
            y_root = find_parent(parent, y)

            if x_root == y_root:
                return

            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

        def is_similar(x, y):
            mismatch = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    mismatch += 1
                    if mismatch > 2:
                        return False
            return True

        n = len(strs)
        parent = [i for i in range(n)]
        rank = [0] * n

        for i in range(n - 1):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    union(parent, rank, i, j)

        groups = set()
        for i in range(n):
            groups.add(find_parent(parent, i))

        return len(groups)
