from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        
        rank_dict = {sorted_score[i]: str(i+1) for i in range(len(sorted_score))}
        
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        result = []
        for s in score:
            rank = rank_dict[s]
            if rank in medals:
                result.append(rank)
            else:
                result.append(rank)
        
        return result
