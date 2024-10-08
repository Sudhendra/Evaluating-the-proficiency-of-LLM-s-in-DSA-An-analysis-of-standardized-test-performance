class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    current_node = stack.pop()
                    for neighbor in graph[current_node]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current_node]
                            stack.append(neighbor)
                        elif color[neighbor] == color[current_node]:
                            return False
        return True