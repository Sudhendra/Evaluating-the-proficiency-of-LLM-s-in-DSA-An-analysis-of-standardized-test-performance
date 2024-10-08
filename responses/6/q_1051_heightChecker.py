from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(1 for h1, h2 in zip(heights, expected) if h1 != h2)
