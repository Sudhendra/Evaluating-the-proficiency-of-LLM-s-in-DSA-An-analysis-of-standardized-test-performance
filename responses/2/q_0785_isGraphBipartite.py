class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}  # Dictionary to store the color of each node, 0 for uncolored, 1 and -1 for two different colors

        def dfs(node, c):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, -c) for nei in graph[node])

        return all(node in color or dfs(node, 1) for node in range(len(graph)) if graph[node])