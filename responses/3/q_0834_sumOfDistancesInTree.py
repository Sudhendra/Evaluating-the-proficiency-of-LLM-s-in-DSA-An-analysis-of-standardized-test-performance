class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node, parent):
            count[node] = 1
            ans[node] = 0
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
                count[node] += count[nei]
                ans[node] += ans[nei] + count[nei]

        def dfs2(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue
                ans[nei] = ans[node] - count[nei] + n - count[nei]
                dfs2(nei, node)

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [0] * n
        ans = [0] * n

        dfs(0, -1)
        dfs2(0, -1)

        return ans

# Time complexity: O(n)
# Space complexity: O(n)
