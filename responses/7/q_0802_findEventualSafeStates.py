class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n
        
        def dfs(node):
            if color[node] == 1:
                return True
            if color[node] == 2:
                return False
            
            color[node] = 1
            for next_node in graph[node]:
                if dfs(next_node) == False:
                    return False
            color[node] = 2
            return True
        
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        
        return res
