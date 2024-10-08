class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_dict = {score: rank for rank, score in enumerate(sorted_score, start=1)}
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = [medals[rank_dict[score] - 1] if rank_dict[score] <= len(medals) else str(rank_dict[score]) for score in score]
        return result
