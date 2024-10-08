from collections import defaultdict

class Solution:
    
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for richer_pair in richer:
            a, b = richer_pair
            graph[b].append(a)
        
        def dfs(node, quietest, memo):
            if node in memo:
                return memo[node]
            
            if not graph[node]:
                memo[node] = node
                return node
            
            if quiet[node] < quiet[quietest]:
                quietest = node
            
            for neigh in graph[node]:
                cand = dfs(neigh, quietest, memo)
                if quiet[cand] < quiet[quietest]:
                    quietest = cand
            
            memo[node] = quietest
            return quietest
        
        n = len(quiet)
        memo = {}
        return [dfs(i, i, memo) for i in range(n)]
