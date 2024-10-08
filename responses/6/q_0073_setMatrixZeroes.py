from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row_has_zero = False
        col_has_zero = False

        # Check if first row has zero
        for j in range(cols):
            if matrix[0][j] == 0:
                row_has_zero = True
                break

        # Check if first column has zero
        for i in range(rows):
            if matrix[i][0] == 0:
                col_has_zero = True
                break

        # Use first row and first column as flags to mark zero rows and columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set zero rows
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0

        # Set zero columns
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0

        # Set first row if necessary
        if row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Set first column if necessary
        if col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0
