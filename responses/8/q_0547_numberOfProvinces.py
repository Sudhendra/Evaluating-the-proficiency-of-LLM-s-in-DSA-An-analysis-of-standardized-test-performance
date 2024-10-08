from typing import List

class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    isConnected[i][j] = isConnected[j][i] = 0
                    dfs(j)

        n = len(isConnected)
        provinces = 0
        for i in range(n):
            if isConnected[i][i] == 1:
                provinces += 1
                dfs(i)
        
        return provinces
