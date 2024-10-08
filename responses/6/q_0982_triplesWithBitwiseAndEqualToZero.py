from typing import List
from collections import Counter

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        n = 1 << 16
        count = [0] * n
        for a in nums:
            for b in nums:
                count[a & b] += 1

        res = 0
        for c in nums:
            for i in range(n):
                if c & i == 0:
                    res += count[i]

        return res
