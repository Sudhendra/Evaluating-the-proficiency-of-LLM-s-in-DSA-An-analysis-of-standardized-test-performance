from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        
        p_count = Counter(p)
        window_size = len(p)
        window_count = Counter(s[:window_size])
        result = []
        
        if window_count == p_count:
            result.append(0)
        
        for i in range(1, len(s) - len(p) + 1):
            if window_count[s[i-1]] > 1:
                window_count[s[i-1]] -= 1
            else:
                del window_count[s[i-1]]
            
            if s[i + window_size - 1] in window_count:
                window_count[s[i + window_size - 1]] += 1
            else:
                window_count[s[i + window_size - 1]] = 1
            
            if window_count == p_count:
                result.append(i)
        
        return result
