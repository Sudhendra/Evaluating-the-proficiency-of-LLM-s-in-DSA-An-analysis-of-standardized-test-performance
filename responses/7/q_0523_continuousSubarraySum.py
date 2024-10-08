from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        prefix_sum = 0
        seen = {0: -1}  # To handle the case where sum is a multiple of k from the start
        for i in range(len(nums)):
            prefix_sum += nums[i]

            if k != 0:
                prefix_sum %= k

            if prefix_sum in seen:
                if i - seen[prefix_sum] > 1:
                    return True
            else:
                seen[prefix_sum] = i

        return False
