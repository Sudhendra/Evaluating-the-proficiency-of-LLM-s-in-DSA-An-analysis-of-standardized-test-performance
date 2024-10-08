from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]) -> int:
        count = defaultdict(int)
        for row in matrix:
            if row[0] == 0:
                count[tuple(row)] += 1
            else:
                count[tuple(1-x for x in row)] += 1
        return max(count.values())
