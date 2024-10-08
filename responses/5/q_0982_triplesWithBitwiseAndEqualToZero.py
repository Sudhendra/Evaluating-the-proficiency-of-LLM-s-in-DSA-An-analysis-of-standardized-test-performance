from typing import List

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        counts = [0] * (1 << 16)
        for num in nums:
            for i in range(1 << 16):
                if i & num == 0:
                    counts[i] += 1

        result = 0
        for i in range(1 << 16):
            for j in range(1 << 16):
                if i & j == 0:
                    result += counts[i] * counts[j]

        return result
