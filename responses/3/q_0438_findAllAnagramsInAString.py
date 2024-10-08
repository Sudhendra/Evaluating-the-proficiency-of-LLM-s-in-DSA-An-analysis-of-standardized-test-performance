from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        result = []
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])

        if p_counter == s_counter:
            result.append(0)

        for i in range(len(p), len(s)):
            if s_counter[s[i - len(p)]] == 1:
                del s_counter[s[i - len(p)]]
            else:
                s_counter[s[i - len(p)]] -= 1
            
            if s[i] in s_counter:
                s_counter[s[i]] += 1
            else:
                s_counter[s[i]] = 1

            if p_counter == s_counter:
                result.append(i - len(p) + 1)
        
        return result