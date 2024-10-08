from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = Counter()
        for row in matrix:
            if row[0] == 1:
                count[tuple(1-x for x in row)] += 1
            else:
                count[tuple(row)] += 1
        return max(count.values())
