from collections import defaultdict
from typing import List

class Solution:
    
    def minStickers(self, stickers: List[str], target: str) -> int:
        n, tar = len(stickers), len(target)
        dp = [-1] * (1 << tar)
        
        for i in range(1 << tar):
            for j in range(n):
                cur = i
                
                for ch in stickers[j]:
                    for k in range(tar):
                        if target[k] == ch and not (cur >> k) & 1:
                            cur |= 1 << k
                            break
                
                if dp[i | cur] == -1 or dp[i | cur] > dp[i] + 1:
                    dp[i | cur] = dp[i] + 1
        
        return dp[(1 << tar) - 1]
