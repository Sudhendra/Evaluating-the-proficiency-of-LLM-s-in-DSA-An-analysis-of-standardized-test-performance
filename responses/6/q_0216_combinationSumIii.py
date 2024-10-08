from itertools import combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        res = [comb for comb in combinations(nums, k) if sum(comb) == n]
        return res
