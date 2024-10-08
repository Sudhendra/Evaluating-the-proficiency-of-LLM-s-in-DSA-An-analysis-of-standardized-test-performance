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
        def is_subsequence_of_others(index, s):
            for i, string in enumerate(strs):
                if i != index and self.is_subsequence(s, string):
                    return True
            return False
        
        strs.sort(key=len, reverse=True)  # Sort strings by length in descending order
        for i, s in enumerate(strs):
            if not any(not self.is_subsequence_of_others(i, s) for i in range(len(strs))):
                return len(s)
        return -1
