class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        def count_set_bits(n):
            count = 0
            while n:
                n &= n - 1
                count += 1
            return count
        
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        count = 0
        for i in range(left, right+1):
            if count_set_bits(i) in primes:
                count += 1
        
        return count