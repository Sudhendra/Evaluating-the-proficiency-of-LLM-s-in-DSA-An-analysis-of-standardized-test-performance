class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0

        char_count = {}

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for char, count in char_count.items():
            if count < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(char))

        return len(s)
