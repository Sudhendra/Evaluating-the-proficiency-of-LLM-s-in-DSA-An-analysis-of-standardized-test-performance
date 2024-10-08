class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7

        def count_ways(s: str) -> int:
            if s[0] == '0':
                return 0
            if s == '*':
                return 9
            if len(s) == 1:
                return 9 if s == '*' else 1

            if s[0] == '*':
                if s[1] == '*':
                    return 9 * 9 + 9  # for '**' case, 9 ways single digit, 9 ways double digits, 9 ways to choose between two digits
                elif s[1] <= '6':
                    return 9 + 2  # for '*1', '*2', '*3', '*4', '*5', '*6'
                else:
                    return 9 + 1  # for '*7', '*8', '*9'
            elif s[1] == '*':
                if s[0] == '1':
                    return 1 + 9  # for '1*', 1 way single digit, 9 ways to choose 2nd digit
                elif s[0] == '2':
                    return 1 + 6  # for '2*', 1 way single digit, 6 ways to choose 2nd digit
                else:
                    return 1  # for other cases like '3*', '4*', ..., '9*'
            elif s[0] == '0':
                return 0
            else:
                return 1 + (9 if s <= '26' else 0)

        prev, current = count_ways(s[0]), count_ways(s[:2])
        for i in range(2, len(s)):
            prev, current = current, (current * count_ways(s[i]) + prev * count_ways(s[i-1:i+1])) % MOD

        return current
