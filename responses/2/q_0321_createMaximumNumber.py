from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge_max(nums1, nums2):
            res = []
            while nums1 or nums2:
                if nums1 > nums2:
                    res.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    res.append(nums2[0])
                    nums2 = nums2[1:]
            return res
        
        def get_max(nums, k):
            stack = []
            n = len(nums)
            drop = n - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        max_num = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            candidate = merge_max(get_max(nums1, i), get_max(nums2, k - i))
            max_num = max(max_num, candidate)
        
        return max_num
