class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def minStickersHelper(stickers, target, memo):
            if target in memo:
                return memo[target]
            
            target_freq = Counter(target)
            min_count = float('inf')
            for sticker in stickers:
                if target[0] not in sticker:
                    continue
                
                next_target = ''
                sticker_freq = Counter(sticker)
                for ch in target:
                    next_target += max(ch, sticker_freq[ch]-target_freq[ch])  # remaining characters needed
            
                count = minStickersHelper(stickers, next_target, memo)
                if count != -1:
                    min_count = min(min_count, 1 + count)
            
            memo[target] = -1 if min_count == float('inf') else min_count
            return memo[target]
        
        memo = {'': 0}
        res = minStickersHelper(stickers, target, memo)
        return res if res != float('inf') else -1