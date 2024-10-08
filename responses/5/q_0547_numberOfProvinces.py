from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]) -> int:
        def dfs(city):
            visited.add(city)
            for connected_city in range(len(isConnected)):
                if isConnected[city][connected_city] == 1 and connected_city not in visited:
                    dfs(connected_city)

        n = len(isConnected)
        provinces = 0
        visited = set()

        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces += 1

        return provinces
