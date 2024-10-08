class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i + self.minSteps(n // i)
        return n