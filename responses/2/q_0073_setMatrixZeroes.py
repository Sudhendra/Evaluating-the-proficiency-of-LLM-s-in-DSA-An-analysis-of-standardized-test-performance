from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        row_zero, col_zero = False, False

        # Check if first row contains zero
        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = True
                break

        # Check if first column contains zero
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
                break

        # Use first row and first column as flags to denote if that row/column needs to be zeroed
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Go through the matrix and set zeros based on flags
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_zero:
            for j in range(n):
                matrix[0][j] = 0

        if col_zero:
            for i in range(m):
                matrix[i][0] = 0
