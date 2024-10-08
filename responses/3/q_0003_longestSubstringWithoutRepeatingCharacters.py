class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_length = 0
        start = 0
        char_index_map = {}

        for i in range(len(s)):
            if s[i] in char_index_map and char_index_map[s[i]] >= start:
                start = char_index_map[s[i]] + 1
            char_index_map[s[i]] = i
            max_length = max(max_length, i - start + 1)

        return max_length