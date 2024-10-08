from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        count = 0
        for i in range(m):
            column = [strs[j][i] for j in range(n)]
            if column != sorted(column):
                count += 1
        return count
