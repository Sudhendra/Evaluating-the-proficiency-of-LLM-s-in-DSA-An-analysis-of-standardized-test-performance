from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        def build_graph(equations, values):
            def add_edge(node1, node2, value):
                if node1 in graph:
                    graph[node1].append((node2, value))
                else:
                    graph[node1] = [(node2, value)]

            for (dividend, divisor), value in zip(equations, values):
                add_edge(dividend, divisor, value)
                add_edge(divisor, dividend, 1 / value)

        def find_path(query):
            start, end = query

            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited = set()

            def dfs(node, target, curr_product):
                if node == target:
                    return curr_product

                visited.add(node)

                for neighbor, value in graph[node]:
                    if neighbor not in visited:
                        result = dfs(neighbor, target, curr_product * value)
                        if result != -1.0:
                            return result

                visited.remove(node)
                return -1.0

            return dfs(start, end, 1.0)

        build_graph(equations, values)
        return [find_path(query) for query in queries]
