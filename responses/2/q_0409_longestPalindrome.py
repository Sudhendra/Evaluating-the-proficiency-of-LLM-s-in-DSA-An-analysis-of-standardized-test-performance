class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        palindrome_length = 0
        odd_count = False

        for count in char_count.values():
            palindrome_length += count // 2 * 2
            if count % 2 == 1:
                odd_count = True

        return palindrome_length + 1 if odd_count else palindrome_length
