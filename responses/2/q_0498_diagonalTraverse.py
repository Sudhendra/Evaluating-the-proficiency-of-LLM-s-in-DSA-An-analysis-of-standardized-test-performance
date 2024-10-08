from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        diagonal_map = {}

        for i in range(m):
            for j in range(n):
                if (i + j) not in diagonal_map:
                    diagonal_map[i + j] = []
                diagonal_map[i + j].append(mat[i][j])

        for k, v in diagonal_map.items():
            if k % 2 == 0:
                result.extend(v[::-1])
            else:
                result.extend(v)

        return result
