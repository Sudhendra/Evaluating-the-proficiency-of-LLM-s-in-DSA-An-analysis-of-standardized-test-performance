from collections import Counter

class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        target_chars = Counter(t)
        required_chars = len(target_chars)
        formed_chars = 0
        window_chars = {}
        
        left, right = 0, 0
        min_length = float('inf')
        result = ""
        
        while right < len(s):
            char = s[right]
            window_chars[char] = window_chars.get(char, 0) + 1
            
            if char in target_chars and window_chars[char] == target_chars[char]:
                formed_chars += 1
            
            while formed_chars == required_chars and left <= right:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left:right+1]
                
                left_char = s[left]
                window_chars[left_char] -= 1
                
                if left_char in target_chars and window_chars[left_char] < target_chars[left_char]:
                    formed_chars -= 1
                
                left += 1
                
            right += 1
        
        return result
