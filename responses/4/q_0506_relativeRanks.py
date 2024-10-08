from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranked_score = sorted(score, reverse=True)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i + 1) for i in range(3, len(score))]
        rank_map = {score: rank for score, rank in zip(ranked_score, ranks)}

        return [rank_map[s] for s in score]
