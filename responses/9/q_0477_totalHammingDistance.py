from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total_distance = 0

        for i in range(32):  # 32-bit integer
            count_ones = 0
            for num in nums:
                count_ones += (num >> i) & 1

            total_distance += count_ones * (n - count_ones)

        return total_distance
