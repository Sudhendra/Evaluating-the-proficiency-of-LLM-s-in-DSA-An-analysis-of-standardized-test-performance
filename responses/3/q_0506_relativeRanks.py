class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        rank_map = {}
        for i, s in enumerate(sorted_score):
            if i < 3:
                rank_map[s] = medals[i]
            else:
                rank_map[s] = str(i + 1)

        return [rank_map[s] for s in score]