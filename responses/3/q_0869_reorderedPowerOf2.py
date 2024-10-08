class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(num):
            count = [0] * 10
            while num > 0:
                count[num % 10] += 1
                num //= 10
            return tuple(count)
        
        target_count = count_digits(n)
        power_of_2 = 1
        for _ in range(30):  # log2(10**9) is around 29.9
            if count_digits(power_of_2) == target_count:
                return True
            power_of_2 *= 2
        return False