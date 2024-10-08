class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        
        def get_unique_substrings_ending_at_char(char):
            return (ord(char) - ord('a') + 1)
        
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        count = 1
        
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
                count += 1
            else:
                count = 1
            
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
        
        return sum(dp)