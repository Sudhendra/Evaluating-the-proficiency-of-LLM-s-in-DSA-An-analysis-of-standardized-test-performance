class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7

        def single_char_ways(s: str) -> int:
            if s == "0":
                return 0
            if s == "*":
                return 9
            return 1 if s != "0" else 0 if s > "2" else 2

        def two_chars_ways(c1: str, c2: str) -> int:
            if c1 == "1":
                return 9 if c2 == "*" else 1
            if c1 == "2":
                if c2 == "*":
                    return 6
                if c2 <= "6":
                    return 1
            return 0

        first, second = 1, single_char_ways(s[0])
        for i in range(1, len(s)):
            temp = second * single_char_ways(s[i]) + first * two_chars_ways(s[i - 1], s[i])
            first, second = second, temp % MOD

        return second
