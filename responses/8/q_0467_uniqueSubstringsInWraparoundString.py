class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        length = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord('a') == (ord(s[i - 1]) - ord('a') + 1) % 26:
                length += 1
            else:
                length = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], length)
        
        return sum(dp)
