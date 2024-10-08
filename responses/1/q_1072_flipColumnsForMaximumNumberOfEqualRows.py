from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = Counter()
        for row in matrix:
            count[tuple(row)] += 1
            count[tuple(1 - cell for cell in row)] += 1
        return max(count.values())
