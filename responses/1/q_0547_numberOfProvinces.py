from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]) -> int:
        def dfs(city):
            visited.add(city)
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        provinces = 0
        visited = set()

        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                provinces += 1

        return provinces
