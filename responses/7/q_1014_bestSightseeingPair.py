from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        prev_best_score = values[0] + 0  # Initialize the best score for the first spot
        
        for j in range(1, len(values)):
            max_score = max(max_score, prev_best_score + values[j] - j)  # Update max_score
            prev_best_score = max(prev_best_score, values[j] + j)  # Update the best score for the current spot
        
        return max_score
