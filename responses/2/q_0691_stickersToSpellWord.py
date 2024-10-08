from collections import Counter
from functools import lru_cache

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        cnt_target = Counter(target)

        @lru_cache(None)
        def dp(mask):
            if mask == 0:
                return 0

            res = float('inf')
            for sticker in stickers:
                next_mask = mask
                for char in sticker:
                    for idx in range(len(target)):
                        if target[idx] == char and (next_mask >> idx) & 1 == 0:
                            next_mask |= 1 << idx
                            break
                
                if mask == next_mask:  # no character in sticker that is needed
                    continue
                
                res = min(res, 1 + dp(next_mask))
            
            return res
        
        ans = dp(0)
        if ans == float('inf'):
            return -1
        return ans