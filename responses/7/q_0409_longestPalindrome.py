class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        
        char_count = Counter(s)
        palindrome_length = 0
        has_odd_char = False
        
        for count in char_count.values():
            if count % 2 == 0:
                palindrome_length += count
            else:
                palindrome_length += count - 1
                has_odd_char = True
        
        if has_odd_char:
            palindrome_length += 1
        
        return palindrome_length
