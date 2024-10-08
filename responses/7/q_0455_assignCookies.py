from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_index = 0
        cookies_index = 0
        content_children = 0
        
        while child_index < len(g) and cookies_index < len(s):
            if s[cookies_index] >= g[child_index]:
                content_children += 1
                child_index += 1
            cookies_index += 1
        
        return content_children
