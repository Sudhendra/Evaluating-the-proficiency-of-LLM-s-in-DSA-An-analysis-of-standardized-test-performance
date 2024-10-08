class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if len(s) < len(t):
            return ""

        required = Counter(t)
        missing = len(t)
        left = 0
        min_len = len(s) + 1
        start_index = 0

        for right, char in enumerate(s):
            if char in required:
                required[char] -= 1
                if required[char] >= 0:
                    missing -= 1

            while missing == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start_index = left

                if s[left] in required:
                    required[s[left]] += 1
                    if required[s[left]] > 0:
                        missing += 1

                left += 1

        if min_len == len(s) + 1:
            return ""
        
        return s[start_index:start_index + min_len]
