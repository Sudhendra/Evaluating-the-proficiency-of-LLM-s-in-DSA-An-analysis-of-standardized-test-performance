from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(left, right):
            res = []
            while left or right:
                if left > right:
                    res.append(left[0])
                    left = left[1:]
                else:
                    res.append(right[0])
                    right = right[1:]
            return res

        def getMax(nums, k):
            res = []
            to_pop = len(nums) - k
            for num in nums:
                while to_pop and res and res[-1] < num:
                    res.pop()
                    to_pop -= 1
                res.append(num)
            return res[:k]

        result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            merged = merge(getMax(nums1, i), getMax(nums2, k - i))
            result = max(result, merged)
        return result
