from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols_to_delete = 0
        for col in range(len(strs[0])):
            for i in range(1, len(strs)):
                if strs[i][col] < strs[i-1][col]:
                    cols_to_delete += 1
                    break
        return cols_to_delete
