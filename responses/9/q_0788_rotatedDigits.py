class Solution:
    def rotatedDigits(self, n: int) -> int:
        good_numbers = 0
        for num in range(1, n+1):
            digits = str(num)
            if any(d in digits for d in ['2', '5', '6', '9']) and not any(d in digits for d in ['3', '4', '7']):
                good_numbers += 1
        return good_numbers
