class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k > 0 and i < len(nums) and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        if k % 2 == 1:
            if i == 0:
                nums.sort()
                nums[0] = -nums[0]
            else:
                if abs(nums[i - 1]) < abs(nums[i]):
                    nums[i - 1] = -nums[i - 1]
                else:
                    nums[i] = -nums[i]
        return sum(nums)