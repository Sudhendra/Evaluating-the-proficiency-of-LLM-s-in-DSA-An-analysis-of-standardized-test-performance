class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        i = len(s) - 2
        
        while i >= 0 and s[i] >= s[i + 1]:
            i -= 1
            
        if i == -1:
            return -1

        j = len(s) - 1
        while s[j] <= s[i]:
            j -= 1
            
        s[i], s[j] = s[j], s[i]
        s[i + 1:] = s[i + 1:][::-1]
        
        result = int(''.join(s))
        return result if result < 2**31 - 1 else -1
