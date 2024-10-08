class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = list(map(int, str(n + 1)))
        length = len(digits)
        
        # Helper function to calculate number of permutations
        def permutation(n: int, r: int) -> int:
            result = 1
            for i in range(n, n - r, -1):
                result *= i
            return result
        
        # Calculate the total permutations without repeated digits
        total = 0
        for i in range(1, length):
            total += 9 * permutation(9, i - 1)
        
        # Calculate the permutations with repeated digits
        visited = set()
        for i, digit in enumerate(digits):
            for j in range(1 if i == 0 else 0, digit):
                if j not in visited:
                    total += permutation(9 - i, length - i - 1)
            if digit in visited:
                break
            visited.add(digit)
        
        return n - total
