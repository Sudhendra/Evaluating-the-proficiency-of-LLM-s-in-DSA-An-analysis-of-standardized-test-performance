class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_len = 0
        start = 0

        for end, char in enumerate(s):
            if char in char_index:
                start = max(start, char_index[char] + 1)
            char_index[char] = end
            max_len = max(max_len, end - start + 1)

        return max_len
