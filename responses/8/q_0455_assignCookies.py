from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content = 0
        cookie = 0
        while content < len(g) and cookie < len(s):
            if s[cookie] >= g[content]:
                content += 1
            cookie += 1
        return content
