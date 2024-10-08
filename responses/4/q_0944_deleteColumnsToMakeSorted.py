from typing import List

class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in zip(*strs):  # iterate over columns
            if list(col) != sorted(col):  # compare if column is not sorted
                count += 1
        return count
