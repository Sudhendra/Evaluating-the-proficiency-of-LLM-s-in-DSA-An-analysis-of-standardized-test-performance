class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def countNumbersLessThanX(x):
            original_x = x
            digits = str(x)
            unique_digits = set(map(int, digits))
            total = 0

            for i in range(len(digits)):
                total += 9 * math.factorial(9) // math.factorial(10 - i - 1)
            
            for i in range(len(digits)):
                for j in range(1 if i == 0 else 0, int(digits[i])):
                    if j in unique_digits:
                        continue
                    total += math.factorial(9 - i) // math.factorial(9 - i - 1)
            
            return original_x - total

        return n - countNumbersLessThanX(n) - sum(countNumbersLessThanX(i) for i in range(1, len(str(n))))