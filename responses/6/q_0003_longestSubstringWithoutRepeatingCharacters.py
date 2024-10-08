class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        char_index_map = {}
        max_len = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_index_map:
                start = max(start, char_index_map[s[end]] + 1)

            char_index_map[s[end]] = end
            max_len = max(max_len, end - start + 1)

        return max_len
