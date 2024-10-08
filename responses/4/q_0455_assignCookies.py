from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = 0  # Pointer for children
        j = 0  # Pointer for cookies
        content_children = 0
        
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                content_children += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return content_children
