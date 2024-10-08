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
                if (i + j) % 2 == 0:
                    if (i + j) not in diagonal_map:
                        diagonal_map[i + j] = [mat[i][j]]
                    else:
                        diagonal_map[i + j].append(mat[i][j])
                else:
                    if (i + j) not in diagonal_map:
                        diagonal_map[i + j] = [mat[i][j]]
                    else:
                        diagonal_map[i + j].insert(0, mat[i][j])

        for k in diagonal_map.keys():
            result.extend(diagonal_map[k])

        return result
