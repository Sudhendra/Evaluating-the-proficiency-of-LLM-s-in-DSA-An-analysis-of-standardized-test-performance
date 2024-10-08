class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        for i in range(1, int((2 * n)**0.5) + 1):
            if (2*n) % i == 0:
                x = (2*n) // i
                if x % 2 == 1 and i <= x // 2:
                    count += 1
        return count