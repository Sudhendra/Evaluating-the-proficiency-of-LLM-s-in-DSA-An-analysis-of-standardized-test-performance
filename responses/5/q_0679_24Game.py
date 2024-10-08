from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 0.001

        def dfs(nums):
            if not nums:
                return False

            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    a, b = nums[i], nums[j]
                    new_nums = [val for idx, val in enumerate(nums) if idx != i and idx != j]
                    
                    if dfs(new_nums + [a + b]) or dfs(new_nums + [a - b]) or dfs(new_nums + [b - a]) or \
                       dfs(new_nums + [a * b]) or (b != 0 and dfs(new_nums + [a / b])) or \
                       (a != 0 and dfs(new_nums + [b / a])):
                        return True
            return False

        return dfs(cards)
