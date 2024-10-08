from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len_str = min(strs, key=len)
        for i in range(len(min_len_str)):
            for s in strs:
                if s[i] != min_len_str[i]:
                    return min_len_str[:i]
        return min_len_str
