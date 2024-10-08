from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        res = ""
        k -= 1

        while n > 0:
            n -= 1
            index, k = divmod(k, factorial(n))
            res += nums.pop(index)
        
        return res
