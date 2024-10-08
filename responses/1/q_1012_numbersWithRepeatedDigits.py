class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def factorial(x):
            result = 1
            while x > 1:
                result *= x
                x -= 1
            return result
        
        def numDupDigitsNoGreaterThanN(num_str):
            n = len(num_str)
            result = 0
            for i in range(1, n):
                result += 9 * factorial(9) // factorial(9 - i)
            seen = set()
            for i, digit in enumerate(num_str):
                for j in range(int(digit) if i == 0 else 0, int(digit)):
                    if j not in seen:
                        result += factorial(9 - i)
                if int(digit) in seen:
                    break
                seen.add(int(digit))
            return n - result
        
        return n - numDupDigitsNoGreaterThanN(str(n))