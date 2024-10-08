class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)
        diff = max_num - min_num - 2*k
        return diff if diff > 0 else 0
