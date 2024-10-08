from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        
        def build_graph(equations, values):
            def add_edge(x, y, val):
                if x in graph:
                    graph[x].append((y, val))
                else:
                    graph[x] = [(y, val)]
            
            for i in range(len(equations)):
                x, y = equations[i]
                val = values[i]
                add_edge(x, y, val)
                add_edge(y, x, 1 / val)
        
        def find_path(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            
            if start == end:
                return 1.0
            
            for neighbor, val in graph[start]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                res = find_path(neighbor, end, visited)
                if res != -1.0:
                    return val * res
            return -1.0
        
        build_graph(equations, values)
        result = []
        for query in queries:
            start, end = query
            result.append(find_path(start, end, set()))
        
        return result
