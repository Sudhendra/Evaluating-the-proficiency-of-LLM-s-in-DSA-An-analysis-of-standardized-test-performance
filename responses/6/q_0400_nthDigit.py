class Solution:
    
    def findNthDigit(self, n: int) -> int:
        n -= 1
        for digits in range(1, 11):  # digits = 1, 2, 3, ..., 10
            count = 9 * 10**(digits - 1) * digits
            if n < count:
                num = 10**(digits - 1) + n // digits
                return int(str(num)[n % digits])

        return -1  # This line will never be reached

