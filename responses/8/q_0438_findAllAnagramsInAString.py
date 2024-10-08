from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)-1])
        start = 0
        for end in range(len(p)-1, len(s)):
            s_counter[s[end]] += 1
            if s_counter == p_counter:
                res.append(start)
            s_counter[s[start]] -= 1
            if s_counter[s[start]] == 0:
                del s_counter[s[start]]
            start += 1
        return res
