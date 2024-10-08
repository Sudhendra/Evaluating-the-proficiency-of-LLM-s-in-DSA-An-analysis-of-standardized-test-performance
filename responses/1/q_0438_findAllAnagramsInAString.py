from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_counter = Counter(p)
        window_counter = Counter(s[:len(p)-1])
        for i in range(len(p) - 1, len(s)):
            window_counter[s[i]] += 1
            if window_counter == p_counter:
                result.append(i - len(p) + 1)
            window_counter[s[i - len(p) + 1]] -= 1
            if window_counter[s[i - len(p) + 1]] == 0:
                del window_counter[s[i - len(p) + 1]]
        return result