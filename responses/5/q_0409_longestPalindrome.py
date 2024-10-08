class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        length = 0
        has_odd = False
        for count in char_count.values():
            length += count // 2 * 2
            if count % 2 == 1:
                has_odd = True
        
        return length + 1 if has_odd else length
