class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if not s or not t:
            return ""

        t_count = Counter(t)
        required_chars = len(t_count)
        formed_chars = 0
        left, right = 0, 0
        window_counts = {}
        ans = float("inf"), None, None

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in t_count and window_counts[char] == t_count[char]:
                formed_chars += 1

            while left <= right and formed_chars == required_chars:
                char = s[left]
                if right - left + 1 < ans[0]:
                    ans = right - left + 1, left, right + 1
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed_chars -= 1
                left += 1

            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]]
