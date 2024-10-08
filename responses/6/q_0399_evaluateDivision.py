from typing import List

class Solution:
    
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = {}
        
        def build_graph(equations, values):
            def add_edge(x, y, value):
                if x in graph:
                    graph[x][y] = value
                else:
                    graph[x] = {y: value}
            
            for (dividend, divisor), value in zip(equations, values):
                add_edge(dividend, divisor, value)
                add_edge(divisor, dividend, 1 / value)
        
        def find_path(start, target):
            if start not in graph or target not in graph:
                return -1.0
            
            visited = set()
            
            def dfs(node, target, product):
                if node == target:
                    return product
                
                visited.add(node)
                for neighbor, value in graph[node].items():
                    if neighbor not in visited:
                        result = dfs(neighbor, target, product * value)
                        if result != -1.0:
                            return result
                
                return -1.0
            
            return dfs(start, target, 1.0)
        
        build_graph(equations, values)
        results = [find_path(start, target) for start, target in queries]
        
        return results
