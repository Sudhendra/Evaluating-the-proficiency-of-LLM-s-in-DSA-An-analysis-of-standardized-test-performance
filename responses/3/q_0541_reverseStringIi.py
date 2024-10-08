class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        i = 0
        while i < len(s):
            chunk = s[i:i + 2*k]
            result += chunk[:k][::-1] + chunk[k:2*k]
            i += 2*k
        return result