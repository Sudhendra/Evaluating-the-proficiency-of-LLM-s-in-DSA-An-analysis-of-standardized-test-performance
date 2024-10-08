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
        def is_uncommon(s, index):
            for i, str_other in enumerate(strs):
                if i == index:
                    continue
                if self.is_subsequence(s, str_other):
                    return False
            return True

        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            if all(not self.is_subsequence(s, other) for j, other in enumerate(strs) if j != i):
                return len(s)
        return -1
