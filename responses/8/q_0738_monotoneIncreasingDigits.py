class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = list(str(n))
        length = len(nums)
        i = 1
        while i < length and nums[i - 1] <= nums[i]:
            i += 1
        if i < length:
            while i > 0 and nums[i - 1] > nums[i]:
                nums[i - 1] = str(int(nums[i - 1]) - 1)
                i -= 1
            nums[i + 1:] = '9' * (length - i - 1)
        return int("".join(nums))
