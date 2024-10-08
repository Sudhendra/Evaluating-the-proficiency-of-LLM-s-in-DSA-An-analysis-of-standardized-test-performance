class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        divisor = 2
        while divisor <= n:
            if n % divisor == 0:
                return divisor + self.minSteps(n // divisor)
            divisor += 1
        return n
