from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = {}
        cols = {}
        count = 0

        def union(x, y, parent):
            parent[find(x, parent)] = find(y, parent)

        def find(x, parent):
            if parent[x] != x:
                parent[x] = find(parent[x], parent)
            return parent[x]

        parent = [i for i in range(len(stones))]

        for i, (x, y) in enumerate(stones):
            if x not in rows:
                rows[x] = i
            else:
                union(i, rows[x], parent)

            if y not in cols:
                cols[y] = i
            else:
                union(i, cols[y], parent)

        for i, p in enumerate(parent):
            if i == p:
                count += 1

        return len(stones) - count
