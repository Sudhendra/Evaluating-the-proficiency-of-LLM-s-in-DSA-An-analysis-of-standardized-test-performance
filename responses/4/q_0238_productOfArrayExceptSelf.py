from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Compute the product of all elements to the left
        left_product = 1
        for i in range(n):
            answer[i] *= left_product
            left_product *= nums[i]

        # Compute the product of all elements to the right
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
