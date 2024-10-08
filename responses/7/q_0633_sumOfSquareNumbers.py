class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c ** 0.5)  # Initialize left and right pointers
        while left <= right:
            current_sum = left ** 2 + right ** 2
            if current_sum == c:  # Check if the sum of squares equals c
                return True
            elif current_sum < c:
                left += 1  # Increment left pointer if sum is too small
            else:
                right -= 1  # Decrement right pointer if sum is too large
        return False
