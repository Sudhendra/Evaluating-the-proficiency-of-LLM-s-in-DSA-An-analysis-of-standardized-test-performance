class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        
        def backtrack(counter):
            total = 0
            for ch in counter:
                if counter[ch] == 0:
                    continue
                total += 1
                counter[ch] -= 1
                total += backtrack(counter)
                counter[ch] += 1
            return total
        
        tile_counter = Counter(tiles)
        return backtrack(tile_counter)