from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_and_count(left: List[int], right: List[int]) -> int:
            count = i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= 2 * right[j]:
                    i += 1
                else:
                    count += len(left) - i
                    j += 1
            return count

        def merge_sort(nums: List[int]) -> int:
            if len(nums) <= 1:
                return 0
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return left + right + merge_and_count(sorted(nums[:mid]), sorted(nums[mid:]))

        return merge_sort(nums)