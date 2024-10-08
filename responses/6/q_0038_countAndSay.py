class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        def say(s):
            result = ""
            count = 1
            i = 1
            while i < len(s):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    result += str(count) + s[i - 1]
                    count = 1
                i += 1
            result += str(count) + s[len(s) - 1]
            return result
        
        prev = "1"
        for _ in range(2, n + 1):
            prev = say(prev)
        
        return prev
