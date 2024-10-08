from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        n_len = len(n_str)
        k = len(digits)

        # Count the numbers with length less than n
        ans = sum(k ** i for i in range(1, n_len))

        # Count the numbers with length equal to n
        for i, digit in enumerate(n_str):
            ans += sum(1 for d in digits if d < digit) * (k ** (n_len - i - 1))
            if digit not in digits:
                break
            if i == n_len - 1:
                ans += 1

        return ans
