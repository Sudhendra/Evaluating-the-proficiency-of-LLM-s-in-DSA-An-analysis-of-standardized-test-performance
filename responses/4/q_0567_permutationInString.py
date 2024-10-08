from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter = Counter(s1)
        window_counter = Counter(s2[:len(s1)])

        for i in range(len(s2) - len(s1) + 1):
            if s1_counter == window_counter:
                return True
            if i + len(s1) < len(s2):
                window_counter[s2[i]] -= 1
                if window_counter[s2[i]] == 0:
                    del window_counter[s2[i]]
                window_counter[s2[i + len(s1)]] += 1

        return False
