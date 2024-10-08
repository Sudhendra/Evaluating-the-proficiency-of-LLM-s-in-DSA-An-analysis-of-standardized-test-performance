from collections import Counter
from functools import lru_cache

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_counter = Counter(target)
        stickers_counters = [Counter(sticker) & target_counter for sticker in stickers]

        @lru_cache(None)
        def dp(target_count):
            if sum(target_count.values()) == 0:
                return 0
            res = float('inf')
            for sticker_count in stickers_counters:
                if sticker_count[target_count.most_common(1)[0][0]] == 0:
                    continue
                diff = Counter(target_count)
                for k, v in sticker_count.items():
                    diff[k] -= v
                res = min(res, dp(diff) + 1)
            return res
        
        result = dp(target_counter)
        return -1 if result == float('inf') else result
