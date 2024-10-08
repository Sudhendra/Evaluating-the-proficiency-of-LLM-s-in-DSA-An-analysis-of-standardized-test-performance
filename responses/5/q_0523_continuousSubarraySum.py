from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        prefix_sum_mod_k = {0: -1}
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num
            if k != 0:
                current_sum %= k

            if current_sum in prefix_sum_mod_k:
                if i - prefix_sum_mod_k[current_sum] > 1:
                    return True
            else:
                prefix_sum_mod_k[current_sum] = i

        return False
