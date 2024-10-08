from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(nums1, nums2):
            return [max(nums1, nums2).pop(0) for _ in range(len(nums1) + len(nums2))]
        
        def max_array(nums, k):
            stack = []
            to_pop = len(nums) - k
            for num in nums:
                while to_pop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    to_pop -= 1
                stack.append(num)
            return stack[:k]
        
        def maxNumberHelper(nums1, nums2, k):
            res = []
            for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
                cand = merge(max_array(nums1, i), max_array(nums2, k - i))
                res = max(res, cand)
            return res
        
        return maxNumberHelper(nums1, nums2, k)
