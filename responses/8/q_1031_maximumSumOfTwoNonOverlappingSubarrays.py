from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        result = 0
        max_sum_first = sum(nums[:firstLen])
        max_sum_second = sum(nums[firstLen:firstLen+secondLen])

        for i in range(len(nums) - firstLen):
            max_sum_first = max(max_sum_first, sum(nums[i:i+firstLen]))
            max_sum_second = max(max_sum_second, sum(nums[i+firstLen:i+firstLen+secondLen]))
            result = max(result, max(max_sum_first + prefix_sum[i+firstLen] - prefix_sum[i], max_sum_second + prefix_sum[i+firstLen+secondLen] - prefix_sum[i+firstLen]))

        return result
