class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k > 0 and i < len(nums) and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        if k > 0:
            if k % 2 == 1:
                nums.sort()
                nums[0] = -nums[0]
        return sum(nums)
