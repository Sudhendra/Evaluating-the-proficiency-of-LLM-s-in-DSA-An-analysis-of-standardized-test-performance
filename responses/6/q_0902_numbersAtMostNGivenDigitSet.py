from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        n_length = len(n_str)
        digits_set = set(digits)
        digits_count = len(digits)
        
        result = sum(digits_count ** i for i in range(1, n_length))

        i = 0
        while i < n_length:
            result += sum(1 for digit in digits if digit < n_str[i])
            
            if n_str[i] not in digits_set:
                break
            
            i += 1
            
            if i == n_length:
                result += 1
                
        return result
