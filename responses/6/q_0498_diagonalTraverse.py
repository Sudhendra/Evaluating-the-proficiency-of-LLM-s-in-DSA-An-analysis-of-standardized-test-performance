from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diagonals = [[] for _ in range(m + n - 1)]
        
        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])
        
        res = []
        for k, diag in enumerate(diagonals):
            if k % 2 == 0:
                res.extend(diag[::-1])
            else:
                res.extend(diag)
        
        return res
