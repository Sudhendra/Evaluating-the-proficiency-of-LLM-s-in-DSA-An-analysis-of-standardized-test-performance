from collections import defaultdict

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0

        dp = defaultdict(int)
        dp[s[0]] = 1
        length = 1

        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
                length += 1
            else:
                length = 1

            dp[s[i]] = max(dp[s[i]], length)

        return sum(dp.values())
