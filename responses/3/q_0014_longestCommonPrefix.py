from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            if all(i < len(s) and s[i] == char for s in strs):
                prefix += char
            else:
                break

        return prefix