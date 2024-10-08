from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        if not mines:
            return (n + 1) // 2

        grid = [[1] * n for _ in range(n)]
        banned = set((x, y) for x, y in mines)

        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        for i in range(n):
            # Left direction
            count = 0
            for j in range(n):
                count = 0 if (i, j) in banned else count + 1
                left[i][j] = count

            # Right direction
            count = 0
            for j in range(n - 1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                right[i][j] = count

            # Up direction
            count = 0
            for j in range(n):
                count = 0 if (j, i) in banned else count + 1
                up[j][i] = count

            # Down direction
            count = 0
            for j in range(n - 1, -1, -1):
                count = 0 if (j, i) in banned else count + 1
                down[j][i] = count

        result = 0
        for i in range(n):
            for j in range(n):
                result = max(result, min(left[i][j], right[i][j], up[i][j], down[i][j]))
                
        return result
