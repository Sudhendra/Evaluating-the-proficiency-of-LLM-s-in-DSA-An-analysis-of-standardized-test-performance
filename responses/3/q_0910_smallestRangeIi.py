class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = nums[-1] - nums[0]
        
        for i in range(len(nums) - 1):
            max_num = max(nums[i] + k, nums[-1] - k)
            min_num = min(nums[0] + k, nums[i + 1] - k)
            min_diff = min(min_diff, max_num - min_num)
        
        return min_diff
