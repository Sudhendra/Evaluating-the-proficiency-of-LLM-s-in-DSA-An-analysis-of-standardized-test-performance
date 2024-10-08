from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        mid = len(nums) // 2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
