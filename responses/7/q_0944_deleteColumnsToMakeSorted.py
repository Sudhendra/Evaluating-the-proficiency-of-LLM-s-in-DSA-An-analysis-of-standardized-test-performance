from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        for col in zip(*strs):
            if list(col) != sorted(col):
                cnt += 1
        return cnt
