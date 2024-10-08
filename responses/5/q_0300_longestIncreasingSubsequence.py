from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        length = 0
        
        for num in nums:
            i = bisect_left(dp, num, 0, length)
            dp[i] = num
            if i == length:
                length += 1
        
        return length
