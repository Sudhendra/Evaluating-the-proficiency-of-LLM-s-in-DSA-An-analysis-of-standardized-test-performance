class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = defaultdict(list)
        for equation in equations:
            if equation[1] == '=':
                x, y = equation[0], equation[3]
                graph[x].append(y)
                graph[y].append(x)
        
        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if neighbor not in colors:
                    if not dfs(neighbor, 1 - color):
                        return False
                elif colors[neighbor] == colors[node]:
                    return False
            return True
        
        colors = {}
        for node in graph:
            if node not in colors and not dfs(node, 0):
                return False
        return True
