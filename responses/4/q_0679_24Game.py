from itertools import permutations
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return math.isclose(nums[0], 24, rel_tol=1e-9)
            
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        next_nums = [nums[k] for k in range(len(nums)) if i != k != j]
                        for op in (operator.add, operator.sub, operator.mul, operator.truediv):
                            if (op is operator.add or op is operator.mul or nums[j] != 0):
                                next_nums.append(op(nums[i], nums[j]))
                                if dfs(next_nums):
                                    return True
                                next_nums.pop()
            return False
        
        if dfs(cards):
            return True
        return False
