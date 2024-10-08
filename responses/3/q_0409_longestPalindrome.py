class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        palindrome_length = 0
        has_odd = False
        for count in char_count.values():
            if count % 2 == 0:
                palindrome_length += count
            else:
                palindrome_length += count - 1
                has_odd = True
        
        if has_odd:
            return palindrome_length + 1
        else:
            return palindrome_length