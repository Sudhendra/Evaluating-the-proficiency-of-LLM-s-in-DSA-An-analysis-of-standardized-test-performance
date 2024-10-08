from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        flat_mat = [elem for row in mat for elem in row]

        reshaped_mat = []
        idx = 0
        for i in range(r):
            reshaped_mat.append(flat_mat[idx:idx+c])
            idx += c

        return reshaped_mat
