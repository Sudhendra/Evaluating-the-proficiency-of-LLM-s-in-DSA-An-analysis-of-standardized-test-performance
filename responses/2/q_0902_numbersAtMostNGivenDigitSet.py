from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        n_len = len(n_str)
        digits_count = len(digits)

        result = sum(digits_count ** i for i in range(1, n_len))

        for i, digit in enumerate(n_str):
            result += sum(1 for d in digits if d < digit) * (digits_count ** (n_len - i - 1))
            if digit not in digits:
                break
            if i == n_len - 1:
                result += 1

        return result
