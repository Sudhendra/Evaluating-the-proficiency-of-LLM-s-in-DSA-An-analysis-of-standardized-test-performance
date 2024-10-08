from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(score)+1)]
        rank_dict = {score: rank for score, rank in zip(sorted_score, ranks)}
        return [rank_dict[s] for s in score]
