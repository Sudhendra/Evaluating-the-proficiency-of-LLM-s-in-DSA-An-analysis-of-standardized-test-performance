class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for _ in range(k):
            min_num = min(nums)
            idx = nums.index(min_num)
            nums[idx] = -nums[idx]
        return sum(nums)
