class Solution:
    def findRelativeRanks(self, score):
        score_sorted = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        rank_dict = {score_sorted[i]: str(i + 1) if i >= 3 else medals[i] for i in range(len(score))}
        
        return [rank_dict[s] for s in score]
