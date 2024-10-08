class Solution:
    
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = list(map(int, str(n+1))) 
        k = len(digits)
        num = k * (k - 1) * 9
        excluded = 9
        s = set()
        for i in range(k):
            for j in range(1 if i == 0 else 0, digits[i]):
                if j in s:
                    continue
                num -= excluded
            if digits[i] in s:
                break
            s.add(digits[i])
            excluded -= 1
        
        return n - num

