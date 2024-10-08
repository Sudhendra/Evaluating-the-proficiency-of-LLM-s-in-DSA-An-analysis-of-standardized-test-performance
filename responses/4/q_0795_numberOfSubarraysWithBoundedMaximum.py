from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_bounded_subarrays(max_val):
            count = 0
            total_count = 0
            for num in nums:
                if num <= max_val:
                    count += 1
                    total_count += count
                else:
                    count = 0
            return total_count

        return count_bounded_subarrays(right) - count_bounded_subarrays(left - 1)
