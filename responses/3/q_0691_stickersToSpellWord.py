import collections

class Solution:
    def minStickers(self, stickers, target):
        """Find the minimum number of stickers needed to spell out the target string."""
        target_counter = collections.Counter(target)

        def dp(mask, stickers, memo):
            if mask == 0:
                return 0

            if memo[mask] != -1:
                return memo[mask]

            min_stickers = float('inf')
            for sticker in stickers:
                new_mask = mask
                for char in sticker:
                    for i in range(len(target)):
                        if char == target[i] and not (new_mask & (1 << i)):
                            new_mask |= 1 << i
                            break

                if new_mask != mask:
                    min_stickers = min(min_stickers, 1 + dp(new_mask, stickers, memo))

            memo[mask] = min_stickers
            return min_stickers

        n = len(target)
        mask = 0
        for i in range(n):
            for sticker in stickers:
                if target[i] in sticker:
                    mask |= 1 << i
                    break

        memo = [-1] * (1 << n)
        memo[0] = 0
        result = dp(mask, stickers, memo)

        return -1 if result == float('inf') else result

# Example usage
solution = Solution()
result = solution.minStickers(["with", "example", "science"], "thehat")
print(result)