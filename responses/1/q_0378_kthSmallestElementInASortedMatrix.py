from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]
        
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            j = n - 1
        
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j + 1)
            
            if count < k:
                left = mid + 1
            else:
                right = mid

        return left
