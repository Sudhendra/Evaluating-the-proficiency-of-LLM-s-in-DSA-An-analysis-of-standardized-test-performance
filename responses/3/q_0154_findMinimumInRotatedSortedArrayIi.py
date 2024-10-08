class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                # Minimum element is in the left half
                right = mid
            elif nums[mid] > nums[right]:
                # Minimum element is in the right half
                left = mid + 1
            else:
                # Handle duplicates by moving the right pointer inward
                right -= 1

        return nums[left]