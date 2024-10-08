from collections import Counter

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def dfs(dp, target, counter):
            if dp[target] != -1:
                return dp[target]
            n = len(target)
            res = float('inf')
            for sticker in stickers:
                if counter[sticker] == 0:
                    continue
                new_counter = dict(counter)
                for char in sticker:
                    if new_counter[char] > 0:
                        new_counter[char] -= 1
                new_target = "".join([char for char in target if new_counter[char] > 0])
                sub_res = dfs(dp, new_target, new_counter)
                if sub_res != -1:
                    res = min(res, 1 + sub_res)
            dp[target] = res if res != float('inf') else -1
            return dp[target]

        if set(target) - set("".join(stickers)):
            return -1
        dp = {target: 0}
        counter = Counter("".join(stickers))
        return dfs(dp, target, counter)
