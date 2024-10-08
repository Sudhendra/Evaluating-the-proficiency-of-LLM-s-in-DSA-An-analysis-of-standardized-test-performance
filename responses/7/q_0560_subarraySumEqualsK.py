from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = {0: 1}
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_sum:
                count += prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return count
