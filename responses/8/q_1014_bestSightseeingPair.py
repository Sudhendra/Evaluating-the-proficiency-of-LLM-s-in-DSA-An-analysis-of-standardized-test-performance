from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_value = values[0]

        for j in range(1, len(values)):
            max_score = max(max_score, max_value + values[j] - j)
            max_value = max(max_value, values[j] + j)

        return max_score
