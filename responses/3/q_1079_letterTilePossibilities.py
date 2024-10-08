class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter

        def backtrack(counter):
            count = 0
            for char, freq in counter.items():
                if freq > 0:
                    counter[char] -= 1
                    count += 1 + backtrack(counter)
                    counter[char] += 1
            return count

        char_counter = Counter(tiles)
        return backtrack(char_counter)