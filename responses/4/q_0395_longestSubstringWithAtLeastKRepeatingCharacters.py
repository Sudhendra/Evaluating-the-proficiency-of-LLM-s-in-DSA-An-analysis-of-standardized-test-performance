class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def longest_substring_helper(s, start, end, k):
            if end - start < k:
                return 0
            
            char_count = {}
            for i in range(start, end):
                char_count[s[i]] = char_count.get(s[i], 0) + 1
            
            for i in range(start, end):
                if char_count[s[i]] < k:
                    return max(longest_substring_helper(s, start, i, k), longest_substring_helper(s, i + 1, end, k))
            
            return end - start
        
        return longest_substring_helper(s, 0, len(s), k)
