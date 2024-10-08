from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        result = []
        
        def backtrack(node, path):
            if node == n - 1:
                result.append(path[:])
                return
            
            for neighbor in graph[node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()

        backtrack(0, [0])
        return result
