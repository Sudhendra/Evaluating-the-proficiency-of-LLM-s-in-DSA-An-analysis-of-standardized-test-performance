from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        n_len = len(n_str)
        dig_len = len(digits)

        result = sum(dig_len ** i for i in range(1, n_len))

        for i in range(n_len):
            result += sum(1 for d in digits if d < n_str[i]) * (dig_len ** (n_len - i - 1))
            if n_str[i] not in digits:
                break
            elif i == n_len - 1:
                result += 1

        return result

# The code above provides a solution for the given problem using dynamic programming principles.
# It iterates through the input number n and calculates the count of positive integers that can be constructed.
