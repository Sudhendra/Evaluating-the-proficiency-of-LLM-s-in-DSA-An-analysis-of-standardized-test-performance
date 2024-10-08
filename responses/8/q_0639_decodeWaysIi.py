class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        
        def valid_char(char):
            return char == '1' or char == '2' or char == '*'
        
        def valid_chars(char1, char2):
            if char1 == '*' and char2 == '*':
                return 15
            elif char1 == '*':
                if int(char2) <= 6:
                    return 2
                else:
                    return 1
            elif char2 == '*':
                if char1 == '1':
                    return 9
                elif char1 == '2':
                    return 6
                else:
                    return 0
            else:
                return int(char1 + char2 >= '10' and char1 + char2 <= '26')
        
        dp = [0]*(len(s)+1)
        dp[0] = 1
        
        if not valid_char(s[0]):
            return 0
        
        if s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 1
        
        for i in range(2, len(s)+1):
            if valid_char(s[i-1]):
                dp[i] += dp[i-1] * valid_chars(s[i-1-1], s[i-1])
                dp[i] %= MOD
            
            if valid_char(s[i-2]) and valid_char(s[i-1]):
                dp[i] += dp[i-2] * valid_chars(s[i-2-1], s[i-2:i])
                dp[i] %= MOD
        
        return dp[-1]
