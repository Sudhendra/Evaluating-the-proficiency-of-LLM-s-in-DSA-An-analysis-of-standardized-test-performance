class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))  # Remove duplicates
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)
