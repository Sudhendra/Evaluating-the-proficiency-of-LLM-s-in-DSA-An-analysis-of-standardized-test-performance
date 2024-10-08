from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # If mid element is greater than the rightmost element, the minimum element is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than the rightmost element, the minimum element is in the left half
            elif nums[mid] < nums[right]:
                right = mid
            # If mid element is equal to the rightmost element, shift the search space towards left
            else:
                right -= 1

        return nums[left]