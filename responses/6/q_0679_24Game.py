from typing import List
import itertools

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def helper(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for a, b, *rest in itertools.permutations(nums):
                for result in {a+b, a-b, a*b, b and a/b} - {0}:
                    if helper([result] + rest):
                        return True
            return False

        return helper(cards)
