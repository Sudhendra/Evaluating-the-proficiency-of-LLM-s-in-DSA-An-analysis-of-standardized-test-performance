class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        
        numbers = [str(i) for i in range(1, n+1)]
        result = ""
        
        k -= 1  # Convert k to 0-based index
        
        for i in range(n, 0, -1):
            index = k // math.factorial(i-1)
            k %= math.factorial(i-1)
            result += numbers.pop(index)
        
        return result