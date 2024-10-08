class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def factorial(x):
            result = 1
            for i in range(1, x + 1):
                result *= i
            return result
        
        def countWithoutRepetition(x):
            digits = [int(d) for d in str(x)]
            unique = len(set(digits))
            length = len(digits)
            result = 9 * factorial(9) // factorial(9 - length + 1)
            result -= 9//unique * factorial(8) // factorial(8 - length + 1)
            i = 1
            while i < length:
                result += 9//unique * factorial(9 - i) // factorial(9 - i - (length - i) + 1)
                unique -= 1
                i += 1
            return x - result
        
        return n - countWithoutRepetition(n)
