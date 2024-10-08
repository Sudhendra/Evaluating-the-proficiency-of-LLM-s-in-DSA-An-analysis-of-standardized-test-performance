class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        
        for i in range(0, len(s), 2*k):
            result.extend(s[i:i+k][::-1] + s[i+k:i+2*k])
        
        return "".join(result)
