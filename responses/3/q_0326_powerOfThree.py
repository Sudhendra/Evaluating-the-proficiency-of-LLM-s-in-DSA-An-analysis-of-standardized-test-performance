class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1 or n == 1.0

    def isPowerOfThreeAlternative(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0
