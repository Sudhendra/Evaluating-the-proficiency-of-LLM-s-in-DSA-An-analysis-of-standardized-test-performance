class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v in richer:
            graph[v].append(u)
        
        def dfs(x):
            if dp[x] is not None:
                return dp[x]
            dp[x] = x
            for y in graph[x]:
                if quiet[dfs(y)] < quiet[dp[x]]:
                    dp[x] = dp[y]
            return dp[x]

        n = len(quiet)
        dp = [None] * n
        return [dfs(i) for i in range(n)]