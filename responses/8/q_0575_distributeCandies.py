class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candies = len(set(candyType))  # Count the number of unique candy types
        return min(unique_candies, len(candyType) // 2)  # Return min of unique_candies and total candies Alice can eat
