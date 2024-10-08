from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                    count += 1
                else:
                    nums[i] = nums[i-1]
                    count += 1
        return count <= 1
