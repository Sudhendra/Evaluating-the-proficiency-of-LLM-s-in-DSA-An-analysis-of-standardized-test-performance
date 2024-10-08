class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)

        diff = max_val - min_val
        result = max(0, diff - 2 * k)

        return result  