from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        all_nums = set(fronts + backs)
        min_good = float('inf')
        
        for i in range(n):
            if fronts[i] == backs[i]:
                all_nums.discard(fronts[i])
            else:
                min_good = min(min_good, fronts[i], backs[i])
        
        return min_good if min_good != float('inf') else 0
