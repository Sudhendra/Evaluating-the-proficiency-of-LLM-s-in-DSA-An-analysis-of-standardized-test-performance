class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}  # Dictionary to store color of each node

        # Helper function to perform DFS traversal
        def dfs(node, c):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node, 0) for node in range(len(graph)) if node not in color)
