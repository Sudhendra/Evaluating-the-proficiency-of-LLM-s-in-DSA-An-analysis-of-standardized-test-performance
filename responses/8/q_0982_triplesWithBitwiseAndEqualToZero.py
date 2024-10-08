from collections import defaultdict
from typing import List

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        result = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                counter[nums[i] & nums[j]] += 1
        for num in nums:
            for key in counter:
                if num & key == 0:
                    result += counter[key]
        return result
