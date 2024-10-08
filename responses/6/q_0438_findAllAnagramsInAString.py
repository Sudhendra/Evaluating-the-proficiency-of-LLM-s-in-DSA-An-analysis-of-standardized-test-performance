from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        s_len = len(s)
        if p_len > s_len:
            return []

        p_counter = Counter(p)
        s_window_counter = Counter()

        result = []

        for i in range(s_len):
            s_window_counter[s[i]] += 1
            if i >= p_len:
                if s_window_counter[s[i - p_len]] == 1:
                    del s_window_counter[s[i - p_len]]
                else:
                    s_window_counter[s[i - p_len]] -= 1

            if s_window_counter == p_counter:
                result.append(i - p_len + 1)

        return result
