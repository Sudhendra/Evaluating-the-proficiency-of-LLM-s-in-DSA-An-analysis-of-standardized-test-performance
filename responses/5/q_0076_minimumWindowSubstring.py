class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) + 1

        left, right = 0, 0
        min_len = float('inf')
        min_start = 0
        chars_to_match = len(t)

        for right, char in enumerate(s):
            if char in char_count:
                if char_count[char] > 0:
                    chars_to_match -= 1
                char_count[char] -= 1

            while chars_to_match == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                if s[left] in char_count:
                    char_count[s[left]] += 1
                    if char_count[s[left]] > 0:
                        chars_to_match += 1

                left += 1

        return "" if min_len == float('inf') else s[min_start:min_start + min_len]
