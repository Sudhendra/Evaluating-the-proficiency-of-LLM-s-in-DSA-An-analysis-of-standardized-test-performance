class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        prime_set_bits = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0

        for num in range(left, right + 1):
            set_bits = bin(num).count('1')
            if set_bits in prime_set_bits:
                count += 1

        return count
