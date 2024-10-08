from collections import defaultdict

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def count_letters(word):
            count = defaultdict(int)
            for letter in word:
                count[letter] += 1
            return count

        def remove_letters(count, word):
            for letter in word:
                if count[letter] > 0:
                    count[letter] -= 1
            return count

        def min_stickers_helper(count, stickers, memo):
            if sum(count.values()) == 0:
                return 0

            if tuple(count.items()) in memo:
                return memo[tuple(count.items())]

            res = float('inf')
            for sticker in stickers:
                if sticker[0] not in count:
                    continue

                next_count = count.copy()
                next_count = remove_letters(next_count, sticker)
                
                if count != next_count:
                    res = min(res, 1 + min_stickers_helper(next_count, stickers, memo))

            memo[tuple(count.items())] = res
            return res

        target_count = count_letters(target)
        stickers_count = [count_letters(sticker) for sticker in stickers]

        memo = {}
        result = min_stickers_helper(target_count, stickers_count, memo)

        return result if result != float('inf') else -1
