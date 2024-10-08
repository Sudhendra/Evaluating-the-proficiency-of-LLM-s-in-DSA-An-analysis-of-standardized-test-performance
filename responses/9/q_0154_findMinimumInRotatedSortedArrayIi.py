front_matter = {
    "qid": 154,
    "title": "Find Minimum in Rotated Sorted Array II",
    "titleSlug": "find-minimum-in-rotated-sorted-array-ii",
    "difficulty": "Hard",
    "tags": ["Array", "Binary Search"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1

        return nums[left]