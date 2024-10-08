class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        i = 0
        while i < len(s):
            result += s[i:i+k][::-1]
            result += s[i+k:i+2*k]
            i += 2*k
        return result
