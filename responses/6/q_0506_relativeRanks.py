from typing import List

class Solution:
    
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_dict = {sorted_score[i]: str(i+1) for i in range(len(sorted_score))}
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = []
        for s in score:
            if rank_dict[s] in ["1", "2", "3"]:
                result.append(medals[int(rank_dict[s])-1])
            else:
                result.append(rank_dict[s])
        return result
