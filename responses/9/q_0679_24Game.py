from itertools import permutations
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ops = ['+', '-', '*', '/']

        def backtrack(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for a, b, *rest in permutations(nums):
                for op in ops:
                    if (op == '/' and b < 1e-6):
                        continue
                    if op in ['+', '*']:
                        permuted = [eval(f'{a} {op} {b}')] + rest
                    else:
                        permuted = [eval(f'{a} {op} {b}'), *rest]
                    if backtrack(permuted):
                        return True
            return False

        return backtrack(cards)
