from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s1, s2):
            i, j = 0, 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                j += 1
            return i == len(s1)
        
        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            if all(not is_subsequence(s, other) for j, other in enumerate(strs) if i != j):
                return len(s)
        return -1
