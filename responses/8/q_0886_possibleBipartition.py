from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [0] * (n + 1)
        for i in range(1, n + 1):
            if color[i] == 0 and not self.dfs(i, 1, color, graph):
                return False
        return True

    def dfs(self, node, c, color, graph):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == c:
                return False
            if color[neighbor] == 0 and not self.dfs(neighbor, -c, color, graph):
                return False
        return True
