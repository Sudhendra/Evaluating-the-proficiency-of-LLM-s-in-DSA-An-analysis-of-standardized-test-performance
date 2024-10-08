from collections import Counter
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_counter = Counter(target)
        
        def dfs(stickers_count):
            if all(stickers_count[char] >= target_counter[char] for char in target_counter):
                return 0
            res = float('inf')
            for sticker in stickers:
                if sticker[0] not in target_counter:
                    continue
                next_sticker_count = Counter(stickers_count)
                for char in sticker:
                    next_sticker_count[char] -= 1
                if next_sticker_count[sticker[0]] < 0:
                    continue
                res = min(res, dfs(next_sticker_count) + 1)
            return res
        
        result = dfs(Counter(''.join(stickers)))
        return result if result != float('inf') else -1
