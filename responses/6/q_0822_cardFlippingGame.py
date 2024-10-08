from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        candidates = {x for x in fronts + backs if x not in same}
        return min(candidates) if candidates else 0
