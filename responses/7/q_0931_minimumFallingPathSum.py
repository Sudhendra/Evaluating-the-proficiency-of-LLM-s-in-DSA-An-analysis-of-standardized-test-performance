from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for i in range(1, n):
            for j in range(n):
                min_val = matrix[i-1][j]
                if j > 0:
                    min_val = min(min_val, matrix[i-1][j-1])
                if j < n-1:
                    min_val = min(min_val, matrix[i-1][j+1])
                matrix[i][j] += min_val
        
        return min(matrix[-1])

# Example usage:
# solution = Solution()
# result = solution.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
# print(result)
