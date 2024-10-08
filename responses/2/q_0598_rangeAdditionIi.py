from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        min_x = min(op[0] for op in ops)
        min_y = min(op[1] for op in ops)

        return min_x * min_y
