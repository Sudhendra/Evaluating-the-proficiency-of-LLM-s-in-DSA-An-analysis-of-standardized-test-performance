from typing import List

class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path, result):
            path.append(node)
            if node == len(graph) - 1:
                result.append(path.copy())
            else:
                for neighbor in graph[node]:
                    dfs(neighbor, path, result)
            path.pop()
        
        result = []
        dfs(0, [], result)
        return result
