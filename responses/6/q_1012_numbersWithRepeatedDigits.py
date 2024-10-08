class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def uniquePermutations(n, k):
            if k == 0:
                return 1
            result = 1
            for i in range(n, n - k, -1):
                result *= i
            return result

        def solve(x):
            digits = [int(d) for d in str(x)]
            unique_count = sum(9 * uniquePermutations(9, i - 1) for i in range(1, len(digits)))
            seen = set()
            for i, digit in enumerate(digits):
                for j in range(0 if i else 1, digit):
                    if j not in seen:
                        unique_count += uniquePermutations(9 - i, len(digits) - i - 1)
                if digit in seen:
                    break
                seen.add(digit)
            
            return x - unique_count
        
        return solve(n)
