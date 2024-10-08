from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            stack = []
            for idx, h in enumerate(heights + [0]):
                while stack and h < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = idx if not stack else idx - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(idx)

        return max_area
