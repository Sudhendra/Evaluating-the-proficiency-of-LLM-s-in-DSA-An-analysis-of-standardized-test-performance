from typing import List

class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)

    def findLUSlength(self, strs: List[str]) -> int:
        def is_unique(sub, strings):
            for s in strings:
                if self.is_subsequence(sub, s):
                    return False
            return True

        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            if all(not self.is_subsequence(s, strs[j]) for j in range(len(strs)) if j != i):
                return len(s)
        return -1
