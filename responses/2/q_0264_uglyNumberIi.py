class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        idx2, idx3, idx5 = 0, 0, 0

        for _ in range(1, n):
            next_ugly = min(ugly_numbers[idx2] * 2, ugly_numbers[idx3] * 3, ugly_numbers[idx5] * 5)
            ug