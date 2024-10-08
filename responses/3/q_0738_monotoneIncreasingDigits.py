class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = list(str(n))
        l = len(nums)
        j = l
        for i in range(l-1, 0, -1):
            if int(nums[i]) < int(nums[i-1]):
                nums[i-1] = str(int(nums[i-1]) - 1)
                j = i
        for i in range(j, l):
            nums[i] = '9'
        return int(''.join(nums))