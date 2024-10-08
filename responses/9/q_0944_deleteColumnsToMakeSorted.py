from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0
        
        n = len(strs)
        m = len(strs[0])
        
        deleted_columns = 0
        for i in range(m):
            column_chars = [strs[j][i] for j in range(n)]
            if column_chars != sorted(column_chars):
                deleted_columns += 1
        
        return deleted_columns
