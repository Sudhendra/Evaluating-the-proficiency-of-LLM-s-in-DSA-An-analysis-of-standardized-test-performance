from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        length = 0
        for count in char_count.values():
            length += count // 2 * 2
            if length % 2 == 0 and count % 2 == 1:
                length += 1
        return length
