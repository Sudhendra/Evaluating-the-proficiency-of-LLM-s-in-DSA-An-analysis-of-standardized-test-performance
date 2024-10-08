class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        first_group_length = len(s) % k
        if first_group_length == 0:
            first_group_length = k
        groups = [s[:first_group_length]]
        for i in range(first_group_length, len(s), k):
            groups.append(s[i:i + k])
        return "-".join(groups)