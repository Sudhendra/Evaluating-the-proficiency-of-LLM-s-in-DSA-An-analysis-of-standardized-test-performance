class Solution:
    def countAndSay(self, n: int) -> str:
        def count_and_say(s):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                result.append(str(count) + s[i])
                i += 1
            return ''.join(result)

        if n == 1:
            return '1'
        
        result = '1'
        for _ in range(2, n + 1):
            result = count_and_say(result)
        
        return result