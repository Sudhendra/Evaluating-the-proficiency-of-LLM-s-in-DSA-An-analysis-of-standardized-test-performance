from typing import List

class Solution:
    """You are given two integer arrays `nums1` and `nums2` of lengths `m` and `n` respectively. `nums1` and `nums2` represent the digits of two numbers. You are also given an integer `k`.

    Create the maximum number of length `k <= m + n` from digits of the two numbers. The relative order of the digits from the same array must be preserved.

    Return an array of the `k` digits representing the answer.

    """

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(list1, list2):
            res = []
            while list1 or list2:
                if list1 > list2:
                    res.append(list1[0])
                    list1 = list1[1:]
                else:
                    res.append(list2[0])
                    list2 = list2[1:]
            return res

        def maxSingleNumber(nums, k):
            stack = []
            to_pop = len(nums) - k
            for num in nums:
                while to_pop and stack and num > stack[-1]:
                    stack.pop()
                    to_pop -= 1
                stack.append(num)
            return stack[:k]

        max_num = []
        for i in range(max(0, k - len(nums1)), min(k, len(nums2)) + 1):
            merged = merge(maxSingleNumber(nums1, k - i), maxSingleNumber(nums2, i))
            max_num = max(max_num, merged)
        return max_num
