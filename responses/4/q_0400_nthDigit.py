class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        
        n -= 1
        digits = 1
        first = 1
        count = 9

        while n > digits * count:
            n -= digits * count
            digits += 1
            first *= 10
            count *= 10

        return int(str(first + n // digits)[n % digits])
