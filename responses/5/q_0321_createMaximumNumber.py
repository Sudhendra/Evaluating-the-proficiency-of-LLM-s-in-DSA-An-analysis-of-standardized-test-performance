from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxSingleNumber(nums, k):
            stack = []
            toPop = len(nums) - k
            for num in nums:
                while toPop and stack and stack[-1] < num:
                    stack.pop()
                    toPop -= 1
                stack.append(num)
            return stack[:k]

        def merge(nums1, nums2):
            result = []
            while nums1 or nums2:
                if nums1 > nums2:
                    result.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    result.append(nums2[0])
                    nums2 = nums2[1:]
            return result

        result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            part1 = maxSingleNumber(nums1, i)
            part2 = maxSingleNumber(nums2, k - i)
            merged = merge(part1, part2)
            result = max(result, merged)
        return result
