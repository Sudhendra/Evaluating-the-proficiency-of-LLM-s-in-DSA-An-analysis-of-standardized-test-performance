class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        max_unique = len(set(s))
        max_length = 0
        
        for num_unique in range(1, max_unique + 1):
            char_count = {}
            left, unique, count_atleast_k = 0, 0, 0
            
            for right in range(len(s)):
                if s[right] not in char_count:
                    char_count[s[right]] = 0
                    unique += 1
                char_count[s[right]] += 1
                
                if char_count[s[right]] == k:
                    count_atleast_k += 1
                
                while unique > num_unique:
                    char_count[s[left]] -= 1
                    if char_count[s[left]] == k - 1:
                        count_atleast_k -= 1
                    if char_count[s[left]] == 0:
                        unique -= 1
                    left += 1
                    
                if unique == num_unique and count_atleast_k == num_unique:
                    max_length = max(max_length, right - left + 1)
        
        return max_length
