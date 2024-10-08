class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 1000000007

        def num_ways(s: str) -> int:
            if s.startswith('0'):
                return 0
            if s == '*':
                return 9
            if len(s) == 1:
                return 9 if s == '*' else 1

            if s[1] == '*':
                if s[0] == '1':
                    return 9 + num_ways(s[2:]) * 9
                elif s[0] == '2':
                    return 6 + num_ways(s[2:]) * 9
                elif s[0] == '*':
                    return 15 + num_ways(s[2:]) * 9
                else:
                    return num_ways(s[2:])
            else:
                if s[0] == '0':
                    return 0
                if int(s[:2]) <= 26:
                    return num_ways(s[1:]) + num_ways(s[2:])
                else:
                    return num_ways(s[1:])

        return num_ways(s) % MOD
