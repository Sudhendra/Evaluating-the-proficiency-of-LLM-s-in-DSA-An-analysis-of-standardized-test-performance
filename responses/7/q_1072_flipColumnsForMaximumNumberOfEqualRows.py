from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = Counter()
        for row in matrix:
            signature = tuple(row) if row[0] == 0 else tuple(1 - cell for cell in row)
            counter[signature] += 1
        return max(counter.values())
