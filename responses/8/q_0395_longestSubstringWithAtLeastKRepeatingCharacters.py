class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        max_unique_chars = len(set(s))
        max_length = 0
        
        for unique_chars in range(1, max_unique_chars + 1):
            char_count = {}
            left, right = 0, 0
            unique_count, count_atleast_k = 0, 0
            
            while right < len(s):
                if unique_count <= unique_chars:
                    if s[right] not in char_count:
                        unique_count += 1
                    char_count[s[right]] = char_count.get(s[right], 0) + 1
                    if char_count[s[right]] == k:
                        count_atleast_k += 1
                    right += 1
                
                else:
                    if char_count[s[left]] == k:
                        count_atleast_k -= 1
                    char_count[s[left]] -= 1
                    if char_count[s[left]] == 0:
                        unique_count -= 1
                    left += 1
                
                if unique_count == unique_chars and count_atleast_k == unique_chars:
                    max_length = max(max_length, right - left)
        
        return max_length
