from typing import List

class Solution:
    def countNumbersLessThanN(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        n_digits = len(n_str)
        digits_count = len(digits)
        
        # Count the numbers with fewer digits than n
        result = sum(digits_count ** i for i in range(1, n_digits))
        
        # Check numbers with the same number of digits as n
        for i, digit in enumerate(n_str):
            result += sum(d < digit for d in digits) * (digits_count ** (n_digits - i - 1))
            if digit not in digits:
                break
        
        return result
