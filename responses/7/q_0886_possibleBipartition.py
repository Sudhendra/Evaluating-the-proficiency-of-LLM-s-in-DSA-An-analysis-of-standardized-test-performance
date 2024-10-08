class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        groups = [0] * (n + 1)

        def dfs(person, group):
            groups[person] = group
            for neighbor in graph[person]:
                if groups[neighbor] == group:
                    return False
                if groups[neighbor] == 0 and not dfs(neighbor, -group):
                    return False
            return True

        for i in range(1, n + 1):
            if groups[i] == 0 and not dfs(i, 1):
                return False
        return True
