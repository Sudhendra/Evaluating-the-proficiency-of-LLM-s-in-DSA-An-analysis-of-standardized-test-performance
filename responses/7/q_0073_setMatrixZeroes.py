from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_zero = set()
        cols_to_zero = set()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        for i in rows_to_zero:
            for j in range(n):
                matrix[i][j] = 0

        for j in cols_to_zero:
            for i in range(m):
                matrix[i][j] = 0
