class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        reverse = True
        for i in range(0, len(s), 2*k):
            if reverse:
                result += s[i:i+k][::-1] + s[i+k:i+2*k]
            else:
                result += s[i:i+2*k]
            reverse = not reverse
        return result
