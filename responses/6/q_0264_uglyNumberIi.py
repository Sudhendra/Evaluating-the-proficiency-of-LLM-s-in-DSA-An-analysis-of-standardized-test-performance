class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        pointer_2 = pointer_3 = pointer_5 = 0

        while len(ugly_numbers) < n:
            next_ugly = min(ugly_numbers[pointer_2] * 2, ugly_numbers[pointer_3] * 3, ugly_numbers[pointer_5] * 5)
            ugly_numbers.append(next_ugly)

            if next_ugly == ugly_numbers[pointer_2] * 2:
                pointer_2 += 1
            if next_ugly == ugly_numbers[pointer_3] * 3:
                pointer_3 += 1
            if next_ugly == ugly_numbers[pointer_5] * 5:
                pointer_5 += 1

        return ugly_numbers[-1]
