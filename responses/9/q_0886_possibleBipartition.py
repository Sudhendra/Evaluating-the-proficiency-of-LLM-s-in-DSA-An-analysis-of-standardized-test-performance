from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        color = {}

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, c):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        for i in range(1, n+1):
            if i not in color and not dfs(i, 0):
                return False
        return True
