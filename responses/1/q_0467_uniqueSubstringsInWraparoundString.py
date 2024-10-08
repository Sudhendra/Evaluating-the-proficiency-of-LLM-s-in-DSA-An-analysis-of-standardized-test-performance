class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        
        max_lengths = [0] * 26
        curr_max = 1
        max_lengths[ord(s[0]) - ord('a')] = 1
        
        for i in range(1, len(s)):
            if ord(s[i]) - ord('a') == (ord(s[i - 1]) - ord('a') + 1) % 26:
                curr_max += 1
            else:
                curr_max = 1
            max_lengths[ord(s[i]) - ord('a')] = max(max_lengths[ord(s[i]) - ord('a')], curr_max)
        
        return sum(max_lengths)