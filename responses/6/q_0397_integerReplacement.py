class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                if n == 3 or bin(n - 1).count('1') < bin(n + 1).count('1'):
                    n -= 1
                else:
                    n += 1
            count += 1
        return count
