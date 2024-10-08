from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        n = len(nums)

        while k > 0 and i < n and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1

        if k > 0:
            if k % 2 == 1:
                if i == 0 or abs(nums[i]) < abs(nums[i - 1]):
                    nums[i] = -nums[i]
                else:
                    nums[i - 1] = -nums[i - 1]

        return sum(nums)