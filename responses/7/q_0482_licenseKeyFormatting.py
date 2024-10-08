class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()  # Remove dashes and convert all characters to uppercase
        n = len(s)
        first_group_len = n % k if n % k != 0 else k  # Calculate length of first group
        result = s[:first_group_len]  # Initialize with first group
        for i in range(first_group_len, n, k):
            result += "-" + s[i:i+k]  # Add dashes between groups
        return result
