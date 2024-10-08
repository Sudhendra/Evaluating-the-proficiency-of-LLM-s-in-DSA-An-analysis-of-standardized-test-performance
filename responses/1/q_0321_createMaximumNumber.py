from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(nums1, nums2):
            res = []
            while nums1 or nums2:
                if nums1 > nums2:
                    res.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    res.append(nums2[0])
                    nums2 = nums2[1:]
            return res

        def maxArray(nums, k):
            stack = []
            to_pop = len(nums) - k
            for num in nums:
                while to_pop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    to_pop -= 1
                stack.append(num)
            return stack[:k]

        res = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            merged = merge(maxArray(nums1, i), maxArray(nums2, k - i))
            res = max(res, merged)
        return res