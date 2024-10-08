from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = Counter(tuple(row) if row[0] == 0 else tuple(1 - x for x in row) for row in matrix)
        return max(count.values())
