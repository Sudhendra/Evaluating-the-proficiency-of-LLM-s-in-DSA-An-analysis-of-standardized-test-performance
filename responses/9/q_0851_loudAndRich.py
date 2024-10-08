from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for x, y in richer:
            graph[y].append(x)
        
        def dfs(node):
            if node not in memo:
                ans = node
                for neighbor in graph[node]:
                    candidate = dfs(neighbor)
                    if quiet[candidate] < quiet[ans]:
                        ans = candidate
                memo[node] = ans
            return memo[node]
        
        memo = {}
        return [dfs(i) for i in range(len(quiet))]
