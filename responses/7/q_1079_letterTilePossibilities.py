from collections import Counter

class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            total = 0
            for letter in counter:
                if counter[letter] == 0:
                    continue
                total += 1  # Count the current combination
                counter[letter] -= 1  # Choose the current letter
                total += backtrack(counter)  # Recur with reduced counter
                counter[letter] += 1  # Unchoose the current letter
            return total

        counter = Counter(tiles)
        return backtrack(counter)
