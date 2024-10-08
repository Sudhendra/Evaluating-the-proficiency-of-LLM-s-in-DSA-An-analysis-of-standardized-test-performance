from itertools import permutations

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            
            for a, b, *rest in permutations(nums):
                for op in (lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y if y != 0 else 0):
                    if op is not None:
                        if op == lambda x, y: x / y and abs(y) < 1e-6:
                            continue

                        if dfs([op(a, b)] + rest):
                            return True

                        if op in (lambda x, y: x + y, lambda x, y: x * y):
                            if dfs([op(b, a)] + rest):
                                return True

            return False
        
        return dfs(cards)
