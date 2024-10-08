from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        counter = Counter(s)
        
        for char, freq in counter.items():
            if freq < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
        
        return len(s)
