from collections import Counter

class Solution:
    
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        count = Counter(s)
        unique_chars = set([char for char, freq in count.items() if freq < k])
        
        if not unique_chars:
            return len(s)
        
        parts = s.split(min(unique_chars), k - 1)
        
        return max(self.longestSubstring(part, k) for part in parts)
