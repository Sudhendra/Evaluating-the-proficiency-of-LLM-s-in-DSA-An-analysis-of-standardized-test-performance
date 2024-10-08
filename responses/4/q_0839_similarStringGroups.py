from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def findParent(parents, i):
            if parents[i] != i:
                parents[i] = findParent(parents, parents[i])
            return parents[i]

        def union(parents, sizes, i, j):
            root_i = findParent(parents, i)
            root_j = findParent(parents, j)
            if root_i == root_j:
                return
            if sizes[root_i] < sizes[root_j]:
                parents[root_i] = root_j
                sizes[root_j] += sizes[root_i]
            else:
                parents[root_j] = root_i
                sizes[root_i] += sizes[root_j]

        def isSimilar(s1, s2):
            diff_count = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 2:
                        return False
            return True

        n = len(strs)
        parents = list(range(n))
        sizes = [1] * n

        for i in range(n):
            for j in range(i + 1, n):
                if isSimilar(strs[i], strs[j]):
                    union(parents, sizes, i, j)

        groups = set()
        for i in range(n):
            groups.add(findParent(parents, i))

        return len(groups)
