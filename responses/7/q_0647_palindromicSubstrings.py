class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandFromCenter(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        total_palindromes = 0
        for i in range(len(s)):
            total_palindromes += expandFromCenter(i, i)  # Odd length palindromes
            total_palindromes += expandFromCenter(i, i + 1)  # Even length palindromes
        
        return total_palindromes
