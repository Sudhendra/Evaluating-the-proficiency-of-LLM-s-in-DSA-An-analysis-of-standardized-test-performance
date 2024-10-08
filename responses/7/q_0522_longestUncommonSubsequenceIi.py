from typing import List

class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def findLUSlength(self, strs: List[str]) -> int:
        def is_unique(s, strs):
            for string in strs:
                if self.is_subsequence(s, string):
                    return False
            return True
        
        strs.sort(key=len, reverse=True)
        for i in range(len(strs)):
            if all(not self.is_subsequence(strs[i], strs[j]) for j in range(len(strs)) if i != j):
                return len(strs[i])
        return -1
