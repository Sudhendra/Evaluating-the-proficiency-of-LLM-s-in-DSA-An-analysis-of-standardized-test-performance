class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        curr_best = values[0] + 0
        
        for j in range(1, len(values)):
            max_score = max(max_score, curr_best + values[j] - j)
            curr_best = max(curr_best, values[j] + j)
        
        return max_score