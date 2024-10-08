from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k > 0 and i < len(nums):
            if nums[i] < 0:
                nums[i] *= -1
                k -= 1
            elif nums[i] == 0:
                k = 0
            else:
                if k % 2 == 0:
                    k = 0
                else:
                    if i == 0 or nums[i] < nums[i - 1]:
                        nums[i] *= -1
                    else:
                        k = 0
                k = 0
            i += 1
        return sum(nums)
