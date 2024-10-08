from typing import List

class Solution:
    
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        str_n = str(n)
        len_n = len(str_n)
        len_digits = len(digits)
        
        # Count the total numbers which have less digits than n
        result = sum(len_digits**exp for exp in range(1, len_n))
        
        for i, digit in enumerate(str_n):
            count = sum(1 for d in digits if d < digit)
            result += count * (len_digits**(len_n-i-1))
            
            if digit not in digits:
                break
            
            if i == len_n - 1:
                result += 1
        
        return result

# Example usage
sol = Solution()
print(sol.atMostNGivenDigitSet(["1", "3", "5", "7"], 100))  # Output: 20
print(sol.atMostNGivenDigitSet(["1", "4", "9"], 1000000000))  # Output: 29523
print(sol.atMostNGivenDigitSet(["7"], 8))  # Output: 1
