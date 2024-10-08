from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_types = len(set(candyType))
        max_to_eat = len(candyType) // 2
        return min(max_types, max_to_eat)
