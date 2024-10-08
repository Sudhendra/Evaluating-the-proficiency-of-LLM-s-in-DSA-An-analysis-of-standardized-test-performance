from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        prev_best = values[0] + 0

        for j in range(1, len(values)):
            max_score = max(max_score, prev_best + values[j] - j)
            prev_best = max(prev_best, values[j] + j)

        return max_score
