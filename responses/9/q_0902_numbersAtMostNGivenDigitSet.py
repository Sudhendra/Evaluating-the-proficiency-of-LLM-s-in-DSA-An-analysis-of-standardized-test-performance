from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        n_len = len(n_str)
        digits_count = len(digits)
        
        total = sum(digits_count ** i for i in range(1, n_len))

        i = 0
        while i < n_len:
            total += sum(1 for d in digits if d < n_str[i]) * digits_count ** (n_len - i - 1)
            if n_str[i] not in digits:
                break
            i += 1

        if i == n_len:
            total += 1

        return total
