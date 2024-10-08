from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(s) < len(p):
            return res

        p_count = {}
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1

        left, right = 0, 0
        count = len(p_count)

        while right < len(s):
            if s[right] in p_count:
                p_count[s[right]] -= 1
                if p_count[s[right]] == 0:
                    count -= 1
            right += 1

            while count == 0:
                if right - left == len(p):
                    res.append(left)
                
                if s[left] in p_count:
                    p_count[s[left]] += 1
                    if p_count[s[left]] > 0:
                        count += 1
                left += 1

        return res