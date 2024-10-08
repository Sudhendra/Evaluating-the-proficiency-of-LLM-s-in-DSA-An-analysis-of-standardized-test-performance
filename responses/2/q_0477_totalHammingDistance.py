from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        n = len(nums)

        for i in range(32):  # 32-bit integer
            count_ones = 0
            for num in nums:
                count_ones += (num >> i) & 1

            total_distance += count_ones * (n - count_ones)

        return total_distance