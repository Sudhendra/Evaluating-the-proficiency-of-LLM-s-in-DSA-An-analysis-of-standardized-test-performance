class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7

        def countSingleDigit(char):
            if char == '0':
                return 0
            if char == '*':
                return 9
            return 1

        def countDoubleDigits(c1, c2):
            if c1 == '0':
                return 0
            if c1 == '1':
                if c2 == '*':
                    return 9
                return 1
            if c1 == '2':
                if c2 == '*':
                    return 6
                if '1' <= c2 <= '6':
                    return 1
            if c1 == '*':
                if c2 == '*':
                    return 15
                if c2 <= '6':
                    return 2
                return 1
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        if s[0] == '0':
            dp[1] = 0
        elif s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = (dp[i-1] * countSingleDigit(s[i-1]) + dp[i-2] * countDoubleDigits(s[i-2], s[i-1])) % MOD

        return dp[n]

#Test cases
solution = Solution()
print(solution.numDecodings("*")) # Output: 9
print(solution.numDecodings("1*")) # Output: 18
print(solution.numDecodings("2*")) # Output: 15
