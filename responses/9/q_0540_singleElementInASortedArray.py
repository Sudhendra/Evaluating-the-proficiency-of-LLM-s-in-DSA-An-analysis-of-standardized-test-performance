from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N - 1

        while left < right:
            mid = left + (right - left) // 2
            is_half_even = (right - mid) % 2 == 0

            if nums[mid] == nums[mid + 1]:
                if is_half_even:
                    left = mid + 2
                else:
                    right = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if is_half_even:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]

        return nums[left]
