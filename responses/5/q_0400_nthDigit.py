class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        n -= 1
        start, digits, size = 1, 1, 9
        while n >= digits * size:
            n -= digits * size
            start *= 10
            digits += 1
            size *= 10

        num = start + n // digits
        return int(str(num)[n % digits])
