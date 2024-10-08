class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_types = min(len(set(candyType)), len(candyType) // 2)
        return max_types
