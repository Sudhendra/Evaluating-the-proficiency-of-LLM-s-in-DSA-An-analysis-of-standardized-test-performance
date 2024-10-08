from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)

        answer = [-1] * n

        def dfs(person):
            if answer[person] >= 0:
                return answer[person]
            answer[person] = person
            for richer_person in graph[person]:
                candidate = dfs(richer_person)
                if quiet[candidate] < quiet[answer[person]]:
                    answer[person] = candidate
            return answer[person]

        for person in range(n):
            dfs(person)

        return answer
