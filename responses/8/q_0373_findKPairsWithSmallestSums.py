from typing import List

class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        pairs = [(u, v) for u in nums1 for v in nums2]
        pairs.sort(key=lambda x: x[0] + x[1])
        return [list(pair) for pair in pairs[:k]]
