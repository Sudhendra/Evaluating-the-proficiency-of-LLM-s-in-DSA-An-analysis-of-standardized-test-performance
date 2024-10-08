from typing import List

class Solution:
    """Given a binary array `nums`, return the maximum number of consecutive `1`'s in the array.

    """

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0

        for num in nums:
            if num == 1:
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0

        return max_ones