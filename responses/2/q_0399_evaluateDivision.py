from typing import List

class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = {}
        
        def build_graph(equations, values):
            for (dividend, divisor), value in zip(equations, values):
                if dividend not in graph:
                    graph[dividend] = {}
                if divisor not in graph:
                    graph[divisor] = {}
                graph[dividend][divisor] = value
                graph[divisor][dividend] = 1 / value
        
        def find_path(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, value in graph[start].items():
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                res = find_path(neighbor, end, visited)
                if res != -1.0:
                    return value * res
            return -1.0
        
        build_graph(equations, values)
        
        results = []
        for query in queries:
            results.append(find_path(query[0], query[1], set()))
        
        return results

