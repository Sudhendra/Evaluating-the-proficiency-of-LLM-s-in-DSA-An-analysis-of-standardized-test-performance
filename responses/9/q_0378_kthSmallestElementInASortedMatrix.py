from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count_less_equal(target: int) -> int:
            count = 0
            row, col = n - 1, 0

            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    count += row + 1
                    col += 1
                else:
                    row -= 1

            return count

        left, right = matrix[0][0], matrix[n - 1][n - 1]

        while left < right:
            mid = left + (right - left) // 2
            count = count_less_equal(mid)

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left
