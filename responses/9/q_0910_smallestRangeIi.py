class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[n-1] - nums[0]

        for i in range(n-1):
            high = max(nums[i]+k, nums[n-1]-k)
            low = min(nums[0]+k, nums[i+1]-k)
            ans = min(ans, high-low)

        return ans
