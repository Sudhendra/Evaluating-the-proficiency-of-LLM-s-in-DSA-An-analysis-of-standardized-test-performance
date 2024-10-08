class Solution:
    
    def numDupDigitsAtMostN(self, n: int) -> int:
        num = n + 1
        digits = []
        while num:
            digits.insert(0, num % 10)
            num //= 10
        
        def permutations(n, r):
            result = 1
            for i in range(n, n - r, -1):
                result *= i
            return result
        
        def unique_permutations(n, r):
            return permutations(n, r) // permutations(r, r)
        
        def count_no_repeated(digits):
            result = 0
            for i in range(1, len(digits)):
                result += 9 * unique_permutations(9, i - 1)
            return result
        
        def count_with_repeated(digits):
            result = 0
            digits_set = set()
            for i in range(len(digits)):
                for j in range(1 if i == 0 else 0, digits[i]):
                    if j not in digits_set:
                        result += unique_permutations(9 - i, len(digits) - i - 1)
                if digits[i] in digits_set:
                    break
                digits_set.add(digits[i])
            return result
        
        return n - count_no_repeated(digits) - 1 + count_with_repeated(digits)

# Unit Test
solution = Solution()
assert solution.numDupDigitsAtMostN(20) == 1
assert solution.numDupDigitsAtMostN(100) == 10
assert solution.numDupDigitsAtMostN(1000) == 262
