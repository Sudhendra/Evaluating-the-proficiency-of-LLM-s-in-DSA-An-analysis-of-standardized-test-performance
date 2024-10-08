from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        banned = set((x, y) for x, y in mines)
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if (i, j) in banned:
                    continue
                left[i][j] = (left[i][j - 1] + 1 if j > 0 else 1)
                up[i][j] = (up[i - 1][j] + 1 if i > 0 else 1)
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) in banned:
                    continue
                right[i][j] = (right[i][j + 1] + 1 if j < n - 1 else 1)
                down[i][j] = (down[i + 1][j] + 1 if i < n - 1 else 1)
        
        result = 0
        for i in range(n):
            for j in range(n):
                result = max(result, min(left[i][j], right[i][j], up[i][j], down[i][j]))
        
        return result
