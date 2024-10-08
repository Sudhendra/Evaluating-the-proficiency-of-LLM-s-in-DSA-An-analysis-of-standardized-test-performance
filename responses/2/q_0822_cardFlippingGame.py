from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        min_good = float('inf')
        for num in fronts + backs:
            if num not in same:
                min_good = min(min_good, num)
        return 0 if min_good == float('inf') else min_good
