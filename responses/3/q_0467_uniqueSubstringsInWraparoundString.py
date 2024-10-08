class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0

        dp = [0] * 26
        maxlengths = {}

        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25):
                length = length + 1
            else:
                length = 1

            index = ord(s[i]) - ord('a')
            dp[index] = max(dp[index], length)

        return sum(dp)