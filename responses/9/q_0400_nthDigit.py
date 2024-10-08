class Solution:
    def findNthDigit(self, n: int) -> int:
        n -= 1
        for digits in range(1, 11):
            first_num = 10**(digits - 1)
            if n < 9 * first_num * digits:
                return int(str(first_num + n//digits)[n % digits])
            n -= 9 * first_num * digits
