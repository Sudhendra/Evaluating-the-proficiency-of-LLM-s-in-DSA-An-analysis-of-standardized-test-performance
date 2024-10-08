from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            count = 0
            for tile in counter:
                if counter[tile] > 0:
                    count += 1
                    counter[tile] -= 1
                    count += backtrack(counter)
                    counter[tile] += 1
            return count
        
        count = 0
        counter = Counter(tiles)
        count += backtrack(counter)
        return count
