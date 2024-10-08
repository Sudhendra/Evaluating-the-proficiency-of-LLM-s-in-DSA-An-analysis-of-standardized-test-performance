from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        result = [0] * n

        # Get product of all elements to the left of i
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # Get product of all elements to the right of i
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # Multiply left_products[i] and right_products[i] to get the result
        for i in range(n):
            result[i] = left_products[i] * right_products[i]

        return result
