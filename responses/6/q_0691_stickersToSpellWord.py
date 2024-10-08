from collections import Counter
from functools import lru_cache

class Solution:
    
    def minStickers(self, stickers: List[str], target: str) -> int:
        @lru_cache(None)
        def dp(t_count):
            if all(val <= 0 for val in t_count.values()):
                return 0
            
            res = float('inf')
            for sticker in stickers:
                new_count = t_count.copy()
                for char in sticker:
                    new_count[char] -= 1
                
                if t_count == new_count:  # Skip stickers that don't contribute
                    continue
                
                res = min(res, dp(new_count) + 1)
            
            return res
        
        target_count = Counter(target)
        res = dp(target_count)
        
        return res if res != float('inf') else -1
