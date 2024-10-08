from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]) -> int:
        if not ops:
            return m * n
        min_x = float('inf')
        min_y = float('inf')
        for op in ops:
            min_x = min(min_x, op[0])
            min_y = min(min_y, op[1])
        return min_x * min_y

# Instantiate the Solution class
sol = Solution()

# Test the example cases
print(sol.maxCount(3, 3, [[2, 2], [3, 3]]))  # Output: 4
print(sol.maxCount(3, 3, [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]))  # Output: 4
print(sol.maxCount(3, 3, []))  # Output: 9
