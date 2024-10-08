class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}  # 0: not colored, 1: color A, -1: color B
        for node in range(len(graph)):
            if node not in color:
                color[node] = 1
                stack = [node]
                while stack:
                    curr = stack.pop()
                    for neighbor in graph[curr]:
                        if neighbor not in color:
                            color[neighbor] = -color[curr]
                            stack.append(neighbor)
                        elif color[neighbor] == color[curr]:
                            return False
        return True
