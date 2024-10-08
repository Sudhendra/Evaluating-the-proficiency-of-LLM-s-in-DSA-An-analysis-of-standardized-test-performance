class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        
        def build_graph(equations, values):
            for (dividend, divisor), value in zip(equations, values):
                if dividend not in graph:
                    graph[dividend] = {divisor: value}
                else:
                    graph[dividend][divisor] = value
                if divisor not in graph:
                    graph[divisor] = {dividend: 1 / value}
                else:
                    graph[divisor][dividend] = 1 / value
        
        def dfs(node, target, visited):
            if node not in graph or node in visited:
                return -1.0
            if node == target:
                return 1.0
            
            visited.add(node)
            for neighbor, value in graph[node].items():
                result = dfs(neighbor, target, visited)
                if result != -1.0:
                    return value * result
            return -1.0
        
        build_graph(equations, values)
        
        results = []
        for dividend, divisor in queries:
            results.append(dfs(dividend, divisor, set()))
        
        return results