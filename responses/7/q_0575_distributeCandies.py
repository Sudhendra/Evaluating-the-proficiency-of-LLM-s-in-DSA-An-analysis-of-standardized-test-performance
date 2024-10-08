from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candies = set(candyType)
        return min(len(unique_candies), len(candyType) // 2)
