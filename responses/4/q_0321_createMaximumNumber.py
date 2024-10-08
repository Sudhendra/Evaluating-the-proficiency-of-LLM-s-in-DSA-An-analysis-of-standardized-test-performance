from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge_max_array(nums1, nums2):
            res = []
            while nums1 or nums2:
                if nums1 > nums2:
                    res.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    res.append(nums2[0])
                    nums2 = nums2[1:]
            return res

        def max_array(nums, k):
            ans = []
            to_pop = len(nums) - k
            for num in nums:
                while to_pop and ans and ans[-1] < num:
                    ans.pop()
                    to_pop -= 1
                ans.append(num)
            return ans[:k]

        def max_number_helper(nums1, nums2, k):
            res = []
            for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
                candidate = merge_max_array(max_array(nums1, i), max_array(nums2, k - i))
                res = max(res, candidate)
            return res

        return max_number_helper(nums1, nums2, k)
