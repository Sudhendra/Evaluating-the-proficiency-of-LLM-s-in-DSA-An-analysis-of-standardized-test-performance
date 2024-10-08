import math

class Solution:
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        for i in range(left, right+1):
            if self.is_prime(bin(i).count('1')):
                count += 1
        return count
