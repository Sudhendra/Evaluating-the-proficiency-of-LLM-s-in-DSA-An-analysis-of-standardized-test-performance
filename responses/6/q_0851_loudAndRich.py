from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for rich, poor in richer:
            graph[poor].append(rich)

        answer = [-1] * n

        def dfs(person):
            if answer[person] == -1:
                answer[person] = person
                for neighbor in graph[person]:
                    candidate = dfs(neighbor)
                    if quiet[candidate] < quiet[answer[person]]:
                        answer[person] = candidate
            return answer[person]

        for person in range(n):
            dfs(person)

        return answer
