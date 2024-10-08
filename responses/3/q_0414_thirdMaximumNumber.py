class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))  # Remove duplicates
        if len(nums) < 3:
            return max(nums)  # Less than 3 distinct numbers, return maximum
        else:
            return sorted(nums)[-3]  # Return the third maximum number
