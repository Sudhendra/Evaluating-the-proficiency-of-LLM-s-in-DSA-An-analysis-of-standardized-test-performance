class Solution:
    def findNthDigit(self, n: int) -> int:
        n -= 1
        for digits in range(1, 11):
            first_num = 10 ** (digits - 1)
            if n < 9 * digits * first_num:
                return int(str(first_num + n//digits)[n%digits])
            n -= 9 * digits * first_num

# Time complexity: O(logn)
# Space complexity: O(1)