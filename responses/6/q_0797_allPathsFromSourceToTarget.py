class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path, result):
            if node == len(graph) - 1:
                result.append(path[:])
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path, result)
                path.pop()
        
        result = []
        dfs(0, [0], result)
        return result
