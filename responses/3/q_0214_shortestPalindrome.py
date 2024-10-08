class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        rev_s = s[::-1]
        new_str = s + "#" + rev_s
        lps = [0] * len(new_str)
        
        j = 0
        for i in range(1, len(new_str)):
            while j > 0 and new_str[i] != new_str[j]:
                j = lps[j-1]
            if new_str[i] == new_str[j]:
                j += 1
            lps[i] = j
        
        return rev_s[:len(s) - lps[-1]] + s