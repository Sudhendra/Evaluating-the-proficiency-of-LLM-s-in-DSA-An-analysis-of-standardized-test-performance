class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_length = 0
        start = 0
        seen = {}
        
        for end, char in enumerate(s):
            if char in seen:
                start = max(start, seen[char] + 1)
            seen[char] = end
            max_length = max(max_length, end - start + 1)
        
        return max_length
