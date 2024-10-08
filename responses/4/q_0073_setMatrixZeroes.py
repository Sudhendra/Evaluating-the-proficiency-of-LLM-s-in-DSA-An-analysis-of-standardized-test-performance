from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_has_zero = False
        col_has_zero = False
        
        # Check if the first row has zero
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                row_has_zero = True
                break
        
        # Check if the first column has zero
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_has_zero = True
                break
        
        # Mark zeros on first row and column
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set zeros based on marks in first row and column
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Set zeros for first row if necessary
        if row_has_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        # Set zeros for first column if necessary
        if col_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
