class Solution:
    def findNthDigit(self, n: int) -> int:
        start, size, step = 1, 1, 9
        while n > size * step:
            n -= size * step
            start *= 10
            size += 1
            step *= 10
        number = start + (n - 1) // size
        return int(str(number)[(n - 1) % size])