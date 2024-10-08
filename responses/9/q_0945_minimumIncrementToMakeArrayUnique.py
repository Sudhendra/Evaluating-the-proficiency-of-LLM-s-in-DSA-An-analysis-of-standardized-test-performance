from collections import Counter

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        taken = 0
        for num, freq in counter.items():
            res += freq * max(0, taken - num)
            taken = max(taken, num) + freq
        return res
