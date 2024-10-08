from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = {0: -1}
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num
            if k != 0:
                current_sum %= k

            if current_sum in prefix_sum:
                if i - prefix_sum[current_sum] > 1:
                    return True
            else:
                prefix_sum[current_sum] = i

        return False
