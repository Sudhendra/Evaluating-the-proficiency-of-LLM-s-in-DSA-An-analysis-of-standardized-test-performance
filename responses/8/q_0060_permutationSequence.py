from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        result = ""
        k -= 1
        
        while n > 0:
            n -= 1
            index, k = divmod(k, factorial(n))
            result += nums.pop(index)
        
        return result
