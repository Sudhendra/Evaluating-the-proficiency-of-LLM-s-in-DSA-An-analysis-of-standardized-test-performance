class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        
        length = len(s)
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        current_length = 1
        
        for i in range(1, length):
            if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
                current_length += 1
            else:
                current_length = 1
            
            index = ord(s[i]) - ord('a')
            dp[index] = max(dp[index], current_length)
        
        return sum(dp)
