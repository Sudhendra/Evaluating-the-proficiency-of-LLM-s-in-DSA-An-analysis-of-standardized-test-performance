class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(num):
            count = [0] * 10
            while num > 0:
                count[num % 10] += 1
                num //= 10
            return tuple(count)
        
        n_count = count_digits(n)
        return any(n_count == count_digits(1 << i) for i in range(31))
