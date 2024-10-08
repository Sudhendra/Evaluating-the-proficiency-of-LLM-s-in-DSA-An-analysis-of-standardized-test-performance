class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
            else:
                nums[i - zero_count] = nums[i]

        for i in range(n - zero_count, n):
            nums[i] = 0