class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter

        def backtrack(counter):
            res = 0
            for char in counter:
                if counter[char] == 0:
                    continue
                res += 1
                counter[char] -= 1
                res += backtrack(counter)
                counter[char] += 1
            return res

        counter = Counter(tiles)
        return backtrack(counter) - 1  # Subtract 1 to exclude the empty sequence
