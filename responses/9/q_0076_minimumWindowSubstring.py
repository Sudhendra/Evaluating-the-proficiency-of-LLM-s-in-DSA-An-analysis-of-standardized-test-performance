class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if not s or not t or len(s) < len(t):
            return ""

        # Create a frequency counter for characters in t
        target_freq = Counter(t)
        required_chars = len(target_freq)
        
        # Initialize window pointers and variables
        left, right = 0, 0
        window_freq = {}
        formed = 0
        ans = (float("inf"), 0, 0)  # (window length, left pointer, right pointer)
        
        while right < len(s):
            # Expand the window to the right
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1
            if char in target_freq and window_freq[char] == target_freq[char]:
                formed += 1
            
            # Contract the window from the left
            while formed == required_chars and left <= right:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right + 1)
                
                left_char = s[left]
                window_freq[left_char] -= 1
                if left_char in target_freq and window_freq[left_char] < target_freq[left_char]:
                    formed -= 1
                
                left += 1
            
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]]
