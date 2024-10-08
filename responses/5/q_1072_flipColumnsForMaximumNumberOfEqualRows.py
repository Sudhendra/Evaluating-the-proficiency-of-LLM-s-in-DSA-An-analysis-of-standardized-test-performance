from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]) -> int:
        counts = defaultdict(int)
        result = 0
        for row in matrix:
            if row[0] == 0:
                counts[tuple(row)] += 1
            else:
                counts[tuple(1-x for x in row)] += 1
        result = max(counts.values())
        return result
