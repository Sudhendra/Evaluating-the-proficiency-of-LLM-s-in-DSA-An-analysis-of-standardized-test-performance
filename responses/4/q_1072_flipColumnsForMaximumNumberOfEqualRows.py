from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counts = {}
        for row in matrix:
            first_val = row[0]
            if first_val == 0:
                row_str = ''.join(map(str, row))
            else:
                row_str = ''.join(map(lambda x: str(1 - x), row))
            counts[row_str] = counts.get(row_str, 0) + 1
        return max(counts.values())
