from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)

        possible_sums = set()
        possible_sums.add(0)

        for num in nums:
            new_possible_sums = set()
            for s in possible_sums:
                new_possible_sums.add(s)
                new_possible_sums.add(s + num)
            possible_sums = new_possible_sums

        for A_size in range(1, n // 2 + 1):
            if total_sum * A_size % n == 0:
                target_sum = total_sum * A_size // n
                if target_sum in possible_sums:
                    return True

        return False
