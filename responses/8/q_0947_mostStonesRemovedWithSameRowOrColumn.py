class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        row_map = {}
        col_map = {}
        
        for i, (x, y) in enumerate(stones):
            row_map[x] = row_map.get(x, []) + [i]
            col_map[y] = col_map.get(y, []) + [i]
        
        for i, (x, y) in enumerate(stones):
            graph[i] = row_map[x] + col_map[y]
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        N = len(stones)
        visited = set()
        components = 0
        
        for i in range(N):
            if i not in visited:
                components += 1
                dfs(i)
        
        return N - components
