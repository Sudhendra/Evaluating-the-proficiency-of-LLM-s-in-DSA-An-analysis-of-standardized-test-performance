class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_prev = values[0]
        
        for i in range(1, len(values)):
            max_score = max(max_score, max_prev + values[i] - i)
            max_prev = max(max_prev, values[i] + i)
        
        return max_score
