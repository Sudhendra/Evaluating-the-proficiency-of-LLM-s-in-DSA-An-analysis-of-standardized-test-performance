class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        if not s:
            return ""

        first_group_len = len(s) % k

        groups = [s[:first_group_len]] if first_group_len > 0 else []
        groups += [s[i:i+k] for i in range(first_group_len, len(s), k)]

        return "-".join(groups)
