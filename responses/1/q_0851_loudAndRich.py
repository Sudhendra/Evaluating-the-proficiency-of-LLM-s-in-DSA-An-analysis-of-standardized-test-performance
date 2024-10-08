from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for u, v in richer:
            graph[v].append(u)
        
        def dfs(node):
            if answers[node] is not None:
                return answers[node]
            curr_ans = node
            for neighbor in graph[node]:
                candidate = dfs(neighbor)
                if quiet[candidate] < quiet[curr_ans]:
                    curr_ans = candidate
            answers[node] = curr_ans
            return curr_ans
                
        answers = [None] * n
        return [dfs(i) for i in range(n)]
