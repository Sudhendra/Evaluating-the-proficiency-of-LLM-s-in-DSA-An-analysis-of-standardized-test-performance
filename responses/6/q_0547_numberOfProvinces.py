from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]) -> int:
        def dfs(node):
            visited.add(node)
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
        
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        for i in range(n):
            if i not in visited:
                provinces += 1
                dfs(i)
        
        return provinces
