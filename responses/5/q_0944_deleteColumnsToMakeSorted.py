from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows, cols = len(strs), len(strs[0])
        result = 0

        for col in range(cols):
            for row in range(1, rows):
                if strs[row][col] < strs[row-1][col]:
                    result += 1
                    break

        return result
