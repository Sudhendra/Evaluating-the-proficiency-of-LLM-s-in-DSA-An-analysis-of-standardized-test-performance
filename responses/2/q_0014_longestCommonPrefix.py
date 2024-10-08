from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        prefix = []
        
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                prefix.append(first[i])
            else:
                break
        
        return "".join(prefix)
