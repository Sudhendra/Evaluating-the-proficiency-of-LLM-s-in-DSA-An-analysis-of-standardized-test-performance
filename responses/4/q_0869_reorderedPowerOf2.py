class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(num):
            result = 0
            while num:
                result += 10 ** (num % 10)
                num //= 10
            return result

        target = count_digits(n)
        return any(count_digits(1 << i) == target for i in range(31))
