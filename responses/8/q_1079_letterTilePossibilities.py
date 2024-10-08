class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from itertools import permutations, chain
        
        return len(set(chain(*[permutations(tiles, i) for i in range(1, len(tiles) + 1)]))
