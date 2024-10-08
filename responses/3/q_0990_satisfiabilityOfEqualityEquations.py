class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = {}
        
        def find(x):
            if x not in graph:
                graph[x] = x
            if graph[x] != x:
                graph[x] = find(graph[x])
            return graph[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                graph[root_x] = root_y
        
        for eq in equations:
            if eq[1] == '=':
                union(eq[0], eq[3])
        
        for eq in equations:
            if eq[1] == '!':
                if find(eq[0]) == find(eq[3]):
                    return False
        
        return True