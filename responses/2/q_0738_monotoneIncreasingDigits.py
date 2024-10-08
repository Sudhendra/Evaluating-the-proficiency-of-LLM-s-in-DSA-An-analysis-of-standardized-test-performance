class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = list(str(n))
        length = len(nums)
        idx = length

        for i in range(length - 1, 0, -1):
            if nums[i - 1] > nums[i]:
                idx = i
                nums[i - 1] = str(int(nums[i - 1]) - 1)

        for i in range(idx, length):
            nums[i] = '9'

        return int("".join(nums))
