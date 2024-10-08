from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = {}
        
        def build_graph(equations, values):
            for (dividend, divisor), value in zip(equations, values):
                if dividend not in adj_list:
                    adj_list[dividend] = {}
                if divisor not in adj_list:
                    adj_list[divisor] = {}
                
                adj_list[dividend][divisor] = value
                adj_list[divisor][dividend] = 1 / value
        
        def dfs(start, target, visited):
            if start not in adj_list or target not in adj_list:
                return -1.0
            
            if start == target:
                return 1.0
            
            if target in adj_list[start]:
                return adj_list[start][target]
            
            visited.add(start)
            for neighbor in adj_list[start]:
                if neighbor not in visited:
                    product = dfs(neighbor, target, visited)
                    if product != -1.0:
                        return adj_list[start][neighbor] * product
            
            return -1.0
        
        build_graph(equations, values)
        results = [dfs(dividend, divisor, set()) for dividend, divisor in queries]
        return results
