from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(num1, num2):
            return [max(num1, num2).pop(0) for _ in range(len(num1) + len(num2))]
        
        def maxArray(nums, k):
            stack = []
            to_pop = len(nums) - k
            for num in nums:
                while to_pop and stack and stack[-1] < num:
                    stack.pop()
                    to_pop -= 1
                stack.append(num)
            return stack[:k]
        
        res = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            merged_nums = merge(maxArray(nums1, i), maxArray(nums2, k - i))
            res = max(res, merged_nums)
        
        return res
