from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_count = Counter(t)
        required_chars = len(t_count)
        formed_chars = 0
        window_counts = {}
        
        left, right = 0, 0
        min_len = float('inf')
        result = ""
        
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in t_count and window_counts[char] == t_count[char]:
                formed_chars += 1
            
            while formed_chars == required_chars and left <= right:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]
                
                window_counts[s[left]] -= 1
                if s[left] in t_count and window_counts[s[left]] < t_count[s[left]]:
                    formed_chars -= 1
                
                left += 1
            
            right += 1
        
        return result
