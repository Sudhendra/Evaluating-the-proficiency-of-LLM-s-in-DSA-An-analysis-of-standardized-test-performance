from itertools import permutations

class Solution:

    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for a, b, *rest in permutations(nums):
                if dfs([a + b] + rest) or dfs([a - b] + rest) or dfs([a * b] + rest):
                    return True
                if b:
                    if dfs([a / b] + rest):
                        return True

            return False

        return dfs(cards)
