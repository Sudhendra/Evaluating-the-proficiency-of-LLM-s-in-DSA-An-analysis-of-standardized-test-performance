from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(parents, i):
            if parents[i] != i:
                parents[i] = find(parents, parents[i])
            return parents[i]

        def union(parents, ranks, i, j):
            root_i = find(parents, i)
            root_j = find(parents, j)
            if ranks[root_i] < ranks[root_j]:
                parents[root_i] = root_j
            elif ranks[root_i] > ranks[root_j]:
                parents[root_j] = root_i
            else:
                parents[root_i] = root_j
                ranks[root_j] += 1

        def is_similar(s1, s2):
            diff_count = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff_count += 1
            return diff_count <= 2

        n = len(strs)
        parents = list(range(n))
        ranks = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]) and find(parents, i) != find(parents, j):
                    union(parents, ranks, i, j)

        groups = set()
        for i in range(n):
            groups.add(find(parents, i))

        return len(groups)