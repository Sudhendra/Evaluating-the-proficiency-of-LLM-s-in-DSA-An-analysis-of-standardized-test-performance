from typing import List

class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            nonlocal isConnected
            nonlocal visited
            
            visited.add(node)
            for neighbor, connected in enumerate(isConnected[node]):
                if connected == 1 and neighbor not in visited:
                    dfs(neighbor)
        
        n = len(isConnected)
        provinces = 0
        visited = set()
        
        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)
        
        return provinces
