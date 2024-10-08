from collections import deque

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            tree[u].append(v)
            tree[v].append(u)

        count = [1] * n
        ans = [0] * n

        def dfs1(node, parent):
            for child in tree[node]:
                if child != parent:
                    dfs1(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node, parent):
            for child in tree[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + n - count[child]
                    dfs2(child, node)

        dfs1(0, -1)
        dfs2(0, -1)

        return ans
