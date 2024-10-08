from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=lambda x: x * 10, reverse=True)
        return str(int(''.join(nums)))
