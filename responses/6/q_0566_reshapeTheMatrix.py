from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        flattened = [val for row in mat for val in row]
        reshaped = [flattened[i*c : (i+1)*c] for i in range(r)]
        
        return reshaped
