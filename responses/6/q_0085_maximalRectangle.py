from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            stack = [-1]
            for k in range(cols):
                while stack[-1] != -1 and heights[k] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = k - 1 - stack[-1]
                    max_area = max(max_area, height * width)
                stack.append(k)

        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = cols - 1 - stack[-1]
            max_area = max(max_area, height * width)

        return max_area
