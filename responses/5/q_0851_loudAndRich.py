class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for x, y in richer:
            graph[y].append(x)

        answer = [-1] * n

        def dfs(person):
            if answer[person] == -1:
                answer[person] = person
                for richer_person in graph[person]:
                    candidate = dfs(richer_person)
                    if quiet[candidate] < quiet[answer[person]]:
                        answer[person] = candidate
            return answer[person]

        for i in range(n):
            dfs(i)

        return answer