from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(node, path):
            if node == len(graph) - 1:
                result.append(path[:])
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()
        
        result = []
        backtrack(0, [0])
        return result
