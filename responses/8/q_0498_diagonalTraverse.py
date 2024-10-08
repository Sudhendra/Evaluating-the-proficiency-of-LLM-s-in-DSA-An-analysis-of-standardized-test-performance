from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        dic = {}

        for i in range(m):
            for j in range(n):
                if (i + j) not in dic:
                    dic[i + j] = [mat[i][j]]
                else:
                    dic[i + j].append(mat[i][j])

        for key in dic:
            if key % 2 == 0:
                result.extend(dic[key][::-1])
            else:
                result.extend(dic[key])

        return result
