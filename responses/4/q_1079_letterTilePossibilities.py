from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            total = 0
            for char in counter:
                if counter[char] == 0:
                    continue
                total += 1
                counter[char] -= 1
                total += backtrack(counter)
                counter[char] += 1
            return total

        counter = Counter(tiles)
        return backtrack(counter)
