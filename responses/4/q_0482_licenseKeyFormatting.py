class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        groups = [s[i:i+k][::-1] for i in range(0, len(s), k)]
        return '-'.join(groups)[::-1]
