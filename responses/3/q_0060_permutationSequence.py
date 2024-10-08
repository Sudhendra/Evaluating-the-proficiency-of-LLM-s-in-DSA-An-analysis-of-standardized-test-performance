class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        from math import factorial
        
        numbers = [str(i) for i in range(1, n+1)]
        result = ""
        k -= 1
        
        while n > 0:
            n -= 1
            index = k // factorial(n)
            result += numbers.pop(index)
            k %= factorial(n)
        
        return result