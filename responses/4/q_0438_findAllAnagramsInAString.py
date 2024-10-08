class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p_counter = Counter(p)
        window_counter = Counter(s[:len(p)])
        result = [] if p_counter != window_counter else [0]

        for i in range(len(p), len(s)):
            window_counter[s[i - len(p)]] -= 1
            if window_counter[s[i - len(p)]] == 0:
                del window_counter[s[i - len(p)]]
            window_counter[s[i]] += 1

            if p_counter == window_counter:
                result.append(i - len(p) + 1)

        return result
