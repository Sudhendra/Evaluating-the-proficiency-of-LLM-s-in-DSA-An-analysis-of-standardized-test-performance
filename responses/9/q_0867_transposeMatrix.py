from typing import List

class Solution:
    """Given a 2D integer array `matrix`, return *the **transpose** of* `matrix`.

    The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
    """

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        transposed = [[0 for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]

        return transposed

# Test cases
print(Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(Solution().transpose([[1, 2, 3], [4, 5, 6]]))  # Output: [[1, 4], [2, 5], [3, 6]]
