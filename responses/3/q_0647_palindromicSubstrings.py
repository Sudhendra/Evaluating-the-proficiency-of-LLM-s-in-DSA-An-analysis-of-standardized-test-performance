class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        for i in range(n):
            count += self.expandFromCenter(s, i, i)  # Odd length palindromes
            count += self.expandFromCenter(s, i, i + 1)  # Even length palindromes
        
        return count
    
    def expandFromCenter(self, s: str, left: int, right: int) -> int:
        count = 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        
        return count