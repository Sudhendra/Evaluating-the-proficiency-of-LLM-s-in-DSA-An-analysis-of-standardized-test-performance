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
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            stack = [-1]
            for k in range(cols):
                while stack[-1] != -1 and heights[k] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = k - stack[-1] - 1
                    max_area = max(max_area, h * w)
                    
                stack.append(k)
        
        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = cols - stack[-1] - 1
            max_area = max(max_area, h * w)
        
        return max_area
