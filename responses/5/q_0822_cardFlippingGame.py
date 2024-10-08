from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        min_good = float('inf')
        same_sides = {num for idx, num in enumerate(fronts) if num == backs[idx]}
        
        for num in fronts + backs:
            if num not in same_sides:
                min_good = min(min_good, num)
        
        return min_good if min_good != float('inf') else 0
