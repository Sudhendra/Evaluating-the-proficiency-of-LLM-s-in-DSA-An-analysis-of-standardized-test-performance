class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_freq = {}
        palindrome_len = 0
        odd_char_count = 0

        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        for count in char_freq.values():
            palindrome_len += count // 2 * 2
            if count % 2 == 1:
                odd_char_count = 1

        return palindrome_len + odd_char_count
