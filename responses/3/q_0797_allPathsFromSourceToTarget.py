from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(path, node):
            if node == len(graph) - 1:
                paths.append(path)
                return
            for nei in graph[node]:
                backtrack(path + [nei], nei)

        paths = []
        backtrack([0], 0)
        return paths
