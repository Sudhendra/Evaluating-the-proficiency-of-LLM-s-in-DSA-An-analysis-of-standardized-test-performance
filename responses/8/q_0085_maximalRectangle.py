from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:  # Check if matrix is empty
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            stack = [-1]
            for k in range(cols+1):
                while heights[k] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = k - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(k)

        return max_area
