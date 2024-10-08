from typing import List

class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = {}
                
        # Build the graph
        def build_graph(eq, val):
            def add_edge(a, b, val):
                if a not in graph:
                    graph[a] = {}
                graph[a][b] = val
                
            for i in range(len(eq)):
                a, b = eq[i][0], eq[i][1]
                add_edge(a, b, val[i])
                add_edge(b, a, 1 / val[i])  # Reverse edge value
                
        build_graph(equations, values)
        
        # DFS search to find the answer
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
                
            if start == end:
                return 1.0
                
            if start in visited:
                return -1.0
                
            visited.add(start)
            for next_node, val in graph[start].items():
                result = dfs(next_node, end, visited)
                if result != -1.0:
                    return val * result
                
            visited.remove(start)
            return -1.0
        
        results = []
        for query in queries:
            results.append(dfs(query[0], query[1], set()))
            
        return results
