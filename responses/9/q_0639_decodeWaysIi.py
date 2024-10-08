class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        def ways1(char):
            if char == '0':
                return 0
            if char == '*':
                return 9
            return 1
        def ways2(char1, char2):
            if char1 == '0':
                return 0
            if char1 == '1':
                if char2 == '*':
                    return 9
                return 1
            if char1 == '2':
                if char2 == '*':
                    return 6
                if '0' <= char2 <= '6':
                    return 1
            if char1 == '*':
                if char2 == '*':
                    return 15
                if '0' <= char2 <= '6':
                    return 2
                return 1
            return 0
        def multiply(a, b):
            return (a * b) % MOD
        dp = [1] + [ways1(s[0])]
        for i in range(1, len(s)):
            dp.append(multiply(dp[-1], ways1(s[i])))
            if s[i-1] != '*' and s[i] != '*':
                dp[-1] = (dp[-1] + multiply(dp[-2], ways2(s[i-1], s[i]))) % MOD
            elif s[i-1] == '*' and s[i] != '*':
                dp[-1] = (dp[-1] + multiply(dp[-2], ways1(s[i]))) % MOD
            elif s[i-1] != '*' and s[i] == '*':
                dp[-1] = (dp[-1] + multiply(dp[-2], ways1(s[i-1]))) % MOD
            else:
                dp[-1] = (dp[-1] + multiply(dp[-2], 15)) % MOD
            if dp[-1] == 0:
                return 0
        return dp[-1]
