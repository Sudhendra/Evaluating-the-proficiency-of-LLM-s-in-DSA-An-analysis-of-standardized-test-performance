from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(node, path):
            if node == len(graph) - 1:
                res.append(path)
            else:
                for neighbor in graph[node]:
                    backtrack(neighbor, path + [neighbor])

        res = []
        backtrack(0, [0])
        return res
