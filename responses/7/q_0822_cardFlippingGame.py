from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same_side = set()
        n = len(fronts)
        for i in range(n):
            if fronts[i] == backs[i]:
                same_side.add(fronts[i])
        
        min_good = float('inf')
        for i in range(n):
            if fronts[i] not in same_side:
                min_good = min(min_good, fronts[i])
            if backs[i] not in same_side:
                min_good = min(min_good, backs[i])
        
        return min_good if min_good != float('inf') else 0
