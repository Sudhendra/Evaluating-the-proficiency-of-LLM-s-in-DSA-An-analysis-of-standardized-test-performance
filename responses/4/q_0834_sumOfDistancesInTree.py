from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        counts = [1] * n
        result = [0] * n

        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def dfs1(node, parent):
            for child in tree[node]:
                if child != parent:
                    dfs1(child, node)
                    counts[node] += counts[child]
                    result[node] += result[child] + counts[child]

        def dfs2(node, parent):
            for child in tree[node]:
                if child != parent:
                    result[child] = result[node] - counts[child] + n - counts[child]
                    dfs2(child, node)

        dfs1(0, -1)
        dfs2(0, -1)

        return result
