from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        def build_graph(equations, values):
            def add_edge(x, y, value):
                if x not in graph:
                    graph[x] = []
                graph[x].append((y, value))

            for (x, y), value in zip(equations, values):
                add_edge(x, y, value)
                add_edge(y, x, 1 / value)

        build_graph(equations, values)

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, value in graph[start]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return value * result
            return -1.0

        results = [dfs(start, end, set()) for start, end in queries]

        return results
