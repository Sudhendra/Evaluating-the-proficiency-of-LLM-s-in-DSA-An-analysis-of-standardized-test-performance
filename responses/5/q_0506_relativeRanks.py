from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranking = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ranks = {ranking[i]: medals[i] if i < 3 else str(i + 1) for i in range(len(ranking))}
        return [ranks[s] for s in score]
