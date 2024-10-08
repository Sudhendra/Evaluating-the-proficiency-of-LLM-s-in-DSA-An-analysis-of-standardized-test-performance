class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = list(str(n))
        length = len(nums)
        i = length - 1
        
        while i > 0:
            if nums[i] < nums[i - 1]:
                nums[i - 1] = str(int(nums[i - 1]) - 1)
                for j in range(i, length):
                    nums[j] = '9'
            i -= 1
        
        return int(''.join(nums))
