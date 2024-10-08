class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)
        diff = max_num - min_num
        return max(0, diff - 2*k)
