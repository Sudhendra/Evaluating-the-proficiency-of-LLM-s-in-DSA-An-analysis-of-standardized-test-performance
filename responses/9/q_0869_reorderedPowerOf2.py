class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def get_digit_count(num):
            count = [0] * 10
            while num > 0:
                count[num % 10] += 1
                num //= 10
            return tuple(count)

        n_count = get_digit_count(n)
        for i in range(31):
            if get_digit_count(1 << i) == n_count:
                return True
        return False
