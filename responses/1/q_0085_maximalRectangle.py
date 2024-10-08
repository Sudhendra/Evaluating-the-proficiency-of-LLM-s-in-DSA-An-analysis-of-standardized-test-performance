class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        def largestRectangleArea(heights):
            stack = []
            heights.append(0)
            max_area = 0
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    idx = stack.pop()
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, heights[idx] * width)
                stack.append(i)
            return max_area
        
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, largestRectangleArea(heights))
        
        return max_area