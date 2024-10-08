from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(x, parent):
            if parent[x] != x:
                parent[x] = find(parent[x], parent)
            return parent[x]

        def union(x, y, parent, rank):
            root_x = find(x, parent)
            root_y = find(y, parent)
            if root_x == root_y:
                return False
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True

        def is_similar(s1, s2):
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                if diff > 2:
                    return False
            return True

        n = len(strs)
        parent = list(range(n))
        rank = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if is_similar(strs[i], strs[j]) and union(i, j, parent, rank):
                    n -= 1

        return n
