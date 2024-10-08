class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        def count_set_bits(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        prime_count = 0
        for num in range(left, right + 1):
            set_bits = count_set_bits(num)
            if is_prime(set_bits):
                prime_count += 1

        return prime_count
