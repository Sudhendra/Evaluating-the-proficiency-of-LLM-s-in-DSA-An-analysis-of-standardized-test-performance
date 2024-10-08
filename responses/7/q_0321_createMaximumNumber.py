from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge_max(nums1, nums2):
            merges = [max(nums1, nums2)]
            while len(nums1) * len(nums2) > 0:
                if nums1 > nums2:
                    nums1 = nums1[1:]
                else:
                    nums2 = nums2[1:]
                merges.append(max(nums1, nums2))
            merges.extend(nums1 or nums2)
            return merges
        
        def max_num(nums, k):
            stack = []
            to_pop = len(nums) - k
            for digit in nums:
                while to_pop and stack and stack[-1] < digit:
                    stack.pop()
                    to_pop -= 1
                stack.append(digit)
            return stack[:k]
        
        max_val = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            max_val = max(max_val, merge_max(max_num(nums1, i), max_num(nums2, k - i)))
        
        return max_val
