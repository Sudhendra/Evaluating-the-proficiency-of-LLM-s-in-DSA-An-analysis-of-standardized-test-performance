class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if not s or not t:
            return ""

        target_counts = Counter(t)
        required_chars = len(target_counts)
        unique_chars = 0
        left, right = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), 0, 0
        
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            while left <= right and formed == required_chars:
                char = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window_counts[char] -= 1
                if char in target_counts and window_counts[char] < target_counts[char]:
                    formed -= 1
                left += 1
            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
