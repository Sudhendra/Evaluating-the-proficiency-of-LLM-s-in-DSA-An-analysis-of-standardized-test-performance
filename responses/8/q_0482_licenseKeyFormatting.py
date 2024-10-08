class Solution:
    
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        if len(s) == 0:
            return ""
        first_group_len = len(s) % k
        groups = [s[:first_group_len]] if first_group_len > 0 else []
        
        for i in range(first_group_len, len(s), k):
            groups.append(s[i:i+k])
        
        return "-".join(groups)
