class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        n = len(s)
        first_group_len = n % k if n % k != 0 else k
        result = s[:first_group_len]
        for i in range(first_group_len, n, k):
            result += "-" + s[i:i+k]
        return result