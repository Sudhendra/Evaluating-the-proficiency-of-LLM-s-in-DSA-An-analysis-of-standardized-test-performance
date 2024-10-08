from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_count = Counter(p)
        s_count = Counter(s[:len(p)-1])

        for i in range(len(p)-1, len(s)):
            s_count[s[i]] += 1

            if s_count == p_count:
                res.append(i - len(p) + 1)

            s_count[s[i - len(p) + 1]] -= 1
            if s_count[s[i - len(p) + 1]] == 0:
                del s_count[s[i - len(p) + 1]]

        return res
