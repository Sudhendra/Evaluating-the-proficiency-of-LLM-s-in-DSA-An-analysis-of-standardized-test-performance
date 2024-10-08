from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        memo = {}
        return self.helper(stone_set, memo, 0, 0)

    def helper(self, stone_set, memo, pos, k):
        if (pos, k) in memo:
            return memo[(pos, k)]

        if pos == stones[-1]:
            return True

        for next_k in [k-1, k, k+1]:
            if next_k > 0 and pos + next_k in stone_set:
                if self.helper(stone_set, memo, pos + next_k, next_k):
                    memo[(pos, k)] = True
                    return True

        memo[(pos, k)] = False
        return False
