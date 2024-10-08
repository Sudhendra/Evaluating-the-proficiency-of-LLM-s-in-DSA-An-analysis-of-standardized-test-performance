from collections import Counter
from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num, freq in count.items():
            if freq == len(nums) // 2:
                return num
