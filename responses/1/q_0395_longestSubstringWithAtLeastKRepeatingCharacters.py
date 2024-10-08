class Solution:

    def longestSubstring(self, s: str, k: int) -> int:
        if not s or k > len(s):
            return 0

        max_unique = len(set(s))
        max_len = 0

        for i in range(1, max_unique+1):
            char_count = {}
            start, end, unique, at_least_k = 0, 0, 0, 0

            while end < len(s):
                if unique <= i:
                    char_count[s[end]] = char_count.get(s[end], 0) + 1
                    if char_count[s[end]] == 1:
                        unique += 1
                    if char_count[s[end]] == k:
                        at_least_k += 1
                    end += 1
                else:
                    char_count[s[start]] -= 1
                    if char_count[s[start]] == 0:
                        unique -= 1
                    if char_count[s[start]] == k - 1:
                        at_least_k -= 1
                    start += 1

                if unique == i and unique == at_least_k:
                    max_len = max(max_len, end - start)

        return max_len
